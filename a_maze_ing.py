import sys


#This gets configurations from the configuration file for use
def get_config(file: str) -> tuple[bool, str]:
    try:
        with open(file, "r") as fd:
            config: str = fd.read()
			return (True, config)
    except (OSError) as error:
		print(
			f"[STDERR] error load_config - {file} - {error}",
			file=sys.stderr
		)
        return (False, f"{error}")


#This loads in the configurations by modifying the config file 
def load_config(file: str, config: str) -> bool:
	try:
		with open(file, "w") as fd:
			fd.write(config)
			return True
	except (OSError) as error:
		print(
			f"[STDERR] error modify_config - {file} - {error}",
			file=sys.stderr
		)
        return False


if __name__ == "__main__":
	if sys.argv[0].startswith("python")
		file_index: int = 2
	else:
		file_index = 1
	if len(sys.argv) != 3:
		print("Usage a_maze_ing.py <file>")
		return
	
	#validate argument
	config: str = get_config(sys.argv[2])
	print(config)
	

	
