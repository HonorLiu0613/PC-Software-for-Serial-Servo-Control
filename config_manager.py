"""
config_manager.py
读取 / 保存 config.json
支持 validate 与默认生成。
"""
import json
from datetime import datetime
from typing import Dict, Any


DEFAULT_DESCRIPTION = "Initial servo angles for the robot."
DEFAULT_VERSION = "1.0"


def default_config(name: str, servos: Dict[str, int]) -> Dict[str, Any]:
    return {
        "name": name or "DanceRobot",
        "description": DEFAULT_DESCRIPTION,
        "version": DEFAULT_VERSION,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "servos": servos
    }


def validate_config(data: Dict[str, Any]) -> bool:
    if "servos" not in data:
        return False
    servos = data["servos"]
    if not isinstance(servos, dict):
        return False
    # Ensure 24 entries (keys "1".."24") and values are ints
    for i in range(1, 25):
        key = str(i)
        if key not in servos:
            return False
        try:
            int(servos[key])
        except Exception:
            return False
    return True


def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not validate_config(data):
        raise ValueError("配置文件格式不符合要求（需要 servos 字段，且包含 1..24）")
    # normalize servo values to ints
    data["servos"] = {str(k): int(v) for k, v in data["servos"].items()}
    return data


def save_config(path: str, name: str, servos: Dict[str, int], description: str = DEFAULT_DESCRIPTION, version: str = DEFAULT_VERSION):
    cfg = default_config(name, servos)
    cfg["description"] = description
    cfg["version"] = version
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=4, ensure_ascii=False)
