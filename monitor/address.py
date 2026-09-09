from __future__ import annotations
import json 

class Address:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    @staticmethod 
    def read_from_json(path: str) -> list[Address]:
        address_list = []
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
        
        for item in data: 
            address_list.append(Address(item["host"], item["port"]))
        return address_list
    
    def __str__(self):
        return f"Host: {self.host}\nPort: {self.port}"