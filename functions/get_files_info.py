import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
	try:
		working_directory = os.path.abspath(working_directory)
		target_directory= os.path.normpath(os.path.join(working_directory, directory))
		valid_target_dir = os.path.commonpath([working_directory, target_directory]) == working_directory

		if not valid_target_dir:
			return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
		
		if not os.path.isdir(target_directory):
			return(f'Error: "{directory}" is not a directory')
		
		directory_items: list[str] = []
		for item in os.listdir(target_directory):
			item_abs = os.path.join(target_directory, item)
			item_size = os.path.getsize(item_abs)
			isdir_item = os.path.isdir(item_abs)

			directory_items.append(f"- {item_abs}: file_size={item_size} bytes, is_dir={isdir_item}")

		return "\n".join(directory_items)
	
	except Exception as e:
		return f"Error: {e}"