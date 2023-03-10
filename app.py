
import docker

#ontainer = client.containers.run('git-image', 'sleep infinity', detach=True, name='git-container')
client = docker.from_env()



container = client.containers.get("1819e298ad20")


cwd = "/"




def terminal(command,cwd):

    """
    Execute a command inside a Docker container with the given working directory.

    Args:
        command (str): The command to execute in the container.
        cwd (str): The working directory to use in the container.

    Returns:
        tuple: A tuple containing the output of the command and the final working
            directory of the container. The output is a string, and the working
            directory is a string representing the absolute path of the directory.
    """
    output = container.exec_run(f'bash -c "cd {cwd} && {command} && pwd"')
  
    output = output.output.decode().split("\n")
    cwd = output[-2]
    return "\n".join(output[:-2]),cwd
 


while True:
    input_str = input('Enter a command (q to quit): ')
    
    # Exit the loop if the user types 'q'
    if input_str == 'q':
        break
    
    response,new_cwd = terminal(input_str,cwd)
    cwd = new_cwd
    print(response)

    # Run the command in the container
    #output = container.exec_run(f'bash -c "cd {cwd} && {input_str} && pwd"')
    
    # Print the output
    #cwd = output.output.decode().split("\n")[-2]
    #print("\n".join(output.output.decode().split("\n")[:-2]))





