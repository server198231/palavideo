import subprocess
import os


def git_commit_and_remove_history():
    try:
        # 自动添加所有更改并提交
        subprocess.run(['git', 'add', '.'], check=True)
        commit_message = "Automated commit"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        # 删除历史提交记录
        # 创建一个新的空分支
        subprocess.run(['git', 'checkout', 'new_branch'], check=True)
        # 添加所有文件
        subprocess.run(['git', 'add', '-A'], check=True)
        # 提交新的初始提交
        subprocess.run(['git', 'commit', '-m', '"init"'], check=True)
        # 删除原来的主分支
        subprocess.run(['git', 'branch', '-D', 'main'], check=True)
        # 将新分支重命名为原来的主分支
        subprocess.run(['git', 'branch', '-m', 'main'], check=True)
        # 强制推送到远程仓库
        subprocess.run(['git', 'push', '-f', 'origin', 'main'], check=True)

        print("代码已成功提交，历史提交记录已删除。")
    except subprocess.CalledProcessError as e:
        print(f"执行 Git 命令时出错: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")


if __name__ == "__main__":
    # 检查当前目录是否为 Git 仓库
    if not os.path.isdir('.git'):
        print("当前目录不是一个 Git 仓库，请在 Git 仓库目录下运行此脚本。")
    else:
        git_commit_and_remove_history()
