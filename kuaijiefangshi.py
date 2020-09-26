import winshell
import os

# my_path=r"D:\winr\fetch_mid_page.bat"
# link_path=r"D:\winr\fmp2.lnk"
#
# with winshell.shortcut(link_path) as link:
#     link.path = my_path
#
# print("done.")

template_str="cmd /k \"cd /d {} && python .\{}\""

target_dir=r"D:\winr"

def main():
    script_path=input("Your script path:")
    link_name=input("Your link name:")
    assert os.sep in script_path
    assert script_path.endswith(".py")
    parts=script_path.rsplit(os.sep,maxsplit=1)
    dir_name,file_name=parts
    bat_str=f"cmd /k \"cd /d {dir_name} && python .\{file_name}\""
    file_name2=file_name.strip(".py")+".bat"

    bat_path=f"{target_dir}{os.sep}{file_name2}"

    with open(bat_path,"w",encoding="utf-8") as f:
        f.write(bat_str)

    link_path=f"{target_dir}{os.sep}{link_name}.lnk"
    with winshell.shortcut(link_path) as link:
        link.path = bat_path

    print("done.")

if __name__ == '__main__':
    main()





