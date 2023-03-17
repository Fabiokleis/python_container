import docker

def main():
    client = docker.from_env()
    rldap = client.containers.get("sleepy_rubin")
    for k,v in rldap.attrs.items():
        print(k,v)

    

if __name__ == "__main__":
    main()
