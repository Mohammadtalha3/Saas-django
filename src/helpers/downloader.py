#This filw ill download the files because in produiction you cannot give out the local-cdn directory so we didi this
import requests
from pathlib import Path


def  download_to_local(url:str, out_path:Path, parent_mkdir:bool= True):
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} is not msut be valid  pathlib  path object")
    
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        response= requests.get(url)
        response.raise_for_status()

        out_path.write_bytes(response.content)
        
        return True
    except requests.RequestException as e:
        print(f'Failed  to download{url}: {e}')
        return False