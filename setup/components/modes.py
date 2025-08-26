"""
Modes component for SuperClaude behavioral modes
"""

from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path

from ..core.base import Component
from setup import __version__
from ..services.claude_md import CLAUDEMdService


class ModesComponent(Component):
    """SuperClaude動作モードコンポーネント"""
    
    def __init__(self, install_dir: Optional[Path] = None):
        """モードコンポーネントを初期化"""
        super().__init__(install_dir, Path(""))
    
    def get_metadata(self) -> Dict[str, str]:
        """コンポーネントメタデータを取得"""
        return {
            "name": "modes",
            "version": __version__,
            "description": "SuperClaude動作モード（ブレインストーミング、内省、タスク管理、トークン効率）",
            "category": "modes"
        }
    
    def _install(self, config: Dict[str, Any]) -> bool:
        """モードコンポーネントをインストール"""
        self.logger.info("SuperClaude動作モードをインストール中...")

        # Validate installation
        success, errors = self.validate_prerequisites()
        if not success:
            for error in errors:
                self.logger.error(error)
            return False

        # Get files to install
        files_to_install = self.get_files_to_install()

        if not files_to_install:
            self.logger.warning("インストールするモードファイルが見つかりません")
            return False

        # Copy mode files
        success_count = 0
        for source, target in files_to_install:
            self.logger.debug(f"Copying {source.name} to {target}")
            
            if self.file_manager.copy_file(source, target):
                success_count += 1
                self.logger.debug(f"Successfully copied {source.name}")
            else:
                self.logger.error(f"Failed to copy {source.name}")

        if success_count != len(files_to_install):
            self.logger.error(f"Only {success_count}/{len(files_to_install)} mode files copied successfully")
            return False

        self.logger.success(f"Modes component installed successfully ({success_count} mode files)")

        return self._post_install()

    def _post_install(self) -> bool:
        """インストール後タスク"""
        try:
            # Update metadata
            metadata_mods = {
                "components": {
                    "modes": {
                        "version": __version__,
                        "installed": True,
                        "files_count": len(self.component_files)
                    }
                }
            }
            self.settings_manager.update_metadata(metadata_mods)
            self.logger.info("モードコンポーネント登録でメタデータを更新しました")
            
            # Update CLAUDE.md with mode imports
            try:
                manager = CLAUDEMdService(self.install_dir)
                manager.add_imports(self.component_files, category="動作モード")
                self.logger.info("モードインポートでCLAUDE.mdを更新しました")
            except Exception as e:
                self.logger.warning(f"モードインポートでCLAUDE.mdの更新に失敗: {e}")
                # Don't fail the whole installation for this
            
            return True
        except Exception as e:
            self.logger.error(f"Failed to update metadata: {e}")
            return False
    
    def uninstall(self) -> bool:
        """モードコンポーネントをアンインストール"""
        try:
            self.logger.info("SuperClaudeモードコンポーネントをアンインストール中...")
            
            # Remove mode files
            removed_count = 0
            for _, target in self.get_files_to_install():
                if self.file_manager.remove_file(target):
                    removed_count += 1
                    self.logger.debug(f"Removed {target.name}")
            
            # Remove modes directory if empty
            try:
                if self.install_component_subdir.exists():
                    remaining_files = list(self.install_component_subdir.iterdir())
                    if not remaining_files:
                        self.install_component_subdir.rmdir()
                        self.logger.debug("空のモードディレクトリを削除しました")
            except Exception as e:
                self.logger.warning(f"モードディレクトリを削除できませんでした: {e}")
            
            # Update settings.json
            try:
                if self.settings_manager.is_component_installed("modes"):
                    self.settings_manager.remove_component_registration("modes")
                    self.logger.info("Removed modes component from settings.json")
            except Exception as e:
                self.logger.warning(f"Could not update settings.json: {e}")
            
            self.logger.success(f"Modes component uninstalled ({removed_count} files removed)")
            return True
            
        except Exception as e:
            self.logger.exception(f"Unexpected error during modes uninstallation: {e}")
            return False
    
    def get_dependencies(self) -> List[str]:
        """Get dependencies"""
        return ["core"]
    
    def _get_source_dir(self) -> Optional[Path]:
        """Get source directory for mode files"""
        # Assume we're in SuperClaude/setup/components/modes.py
        # and mode files are in SuperClaude/SuperClaude/Modes/
        project_root = Path(__file__).parent.parent.parent
        modes_dir = project_root / "SuperClaude" / "Modes"
        
        # Return None if directory doesn't exist to prevent warning
        if not modes_dir.exists():
            return None
        
        return modes_dir
    
    def get_size_estimate(self) -> int:
        """Get estimated installation size"""
        source_dir = self._get_source_dir()
        total_size = 0
        
        if source_dir and source_dir.exists():
            for filename in self.component_files:
                file_path = source_dir / filename
                if file_path.exists():
                    total_size += file_path.stat().st_size
        
        # Minimum size estimate
        total_size = max(total_size, 20480)  # At least 20KB
        
        return total_size
