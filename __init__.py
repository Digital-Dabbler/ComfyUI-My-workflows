# 导入所需的标准库
import os  # 用于文件和目录操作
import json  # 用于JSON数据的序列化和反序列化

class My_workflows:
    """自定义工作流节点类
    
    这个类实现了一个ComfyUI自定义节点，用于管理和存储工作流的描述信息。
    它将工作流的描述保存在一个独立的元数据文件中，便于后续查看和管理。
    """
    
    @classmethod
    def INPUT_TYPES(s):
        """定义节点的输入参数类型
        
        返回：
            dict: 包含两个必需参数：
                - workflow: 工作流文件名
                - description: 工作流描述文本，支持多行输入
        """
        return {
            "required": {
                # 工作流文件名输入字段
                "workflow": ("STRING", {"default": "none"}),
                # 工作流描述输入字段，支持多行文本
                "description": ("STRING", {"multiline": True, "default": "在此输入工作流的描述信息"})
            }
        }

    # 定义节点的返回类型（本节点不需要返回值）
    RETURN_TYPES = ()
    # 指定要调用的函数名
    FUNCTION = "load_workflow"
    # 设置节点在UI中的分类
    CATEGORY = "My_workflows"

    def load_workflow(self, workflow, description):
        """保存工作流的描述信息
        
        Args:
            workflow (str): 工作流文件名
            description (str): 工作流的描述文本
        
        Returns:
            tuple: 空元组，因为不需要返回值
        """
        # 构建工作流文件的完整路径
        workflow_path = os.path.join(WORKFLOW_DIR, workflow)
        # 构建元数据文件的完整路径（使用.meta.json后缀）
        metadata_path = os.path.join(WORKFLOW_DIR, f"{workflow}.meta.json")
        
        # 只有当工作流文件存在时才保存描述
        if os.path.exists(workflow_path):
            # 创建元数据字典
            metadata = {
                "description": description
            }
            # 将元数据保存为JSON文件，使用UTF-8编码以支持中文
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
                
        return ()

# 设置工作流文件存储目录
WORKFLOW_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "example_workflows")

# 向ComfyUI注册自定义节点
NODE_CLASS_MAPPINGS = {
    "My_workflows": My_workflows  # 注册My_workflows类作为自定义节点
}

# 指定Web界面可访问的目录名
WEB_DIRECTORY = os.path.basename(WORKFLOW_DIR)  # 使用目录名作为Web访问路径

# 确保工作流存储目录存在，如果不存在则创建
if not os.path.exists(WORKFLOW_DIR):
    os.makedirs(WORKFLOW_DIR, exist_ok=True)  # 使用exist_ok=True避免并发创建问题