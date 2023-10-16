import subprocess


def call(cmd):
    print(f'>>> {cmd}')
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    tag_name = input("enter tag name (equals to grafana version): ").replace('\n', '')

    call("podman login docker.io")
    call(f"podman build -t docker.io/highwaychile/docker-influxdb-grafana:{tag_name} -f Dockerfile")
    call(f"podman push highwaychile/docker-influxdb-grafana:{tag_name}")