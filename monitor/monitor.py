from monitor.address import Address
import a2s

class Monitor:
    def __init__(self, addresses: list) -> None:
        """
        Initializes the Monitor class with a list of Address objects.
        
        Args:
            addresses (list): A list of Address objects to monitor.
            
        Raises:
            TypeError: If any object in the provided list is not of type Address.    
        """
        
        for i in addresses:
            if not isinstance(i, Address):
                raise TypeError("The provided object is not of type"
                                "\"Address\"")
        self.__addresses = addresses
            
    def __get_info(self) -> list:
        """
        Retrieves server information for each address in the monitor's 
        list of addresses.
        
        Returns:
            list: A list of tuples containing server information and the
            corresponding address.
        """
        
        server_info = []

        for i in self.__addresses:
            address = (i.host, i.port)
            try:
                info = a2s.info(address)
                server_info.append((info, address))
            except:
                server_info.append(({"Error": "Server unreachable"}, (address)))

        return server_info
    
    def fetch(self) -> list[dict]:
        """
        Fetches server information for all addresses in the monitor's list.
        
        Returns:
            list: A list of dictionaries containing server information and
            status for each address.    
        """
        servers = []

        for info, address in self.__get_info():
            if isinstance(info, dict) and "Error" in info:
                servers.append({
                    "status": "Server unreachable",
                    "server_address": address[0],
                    "server_port": address[1],
                })
                continue

            servers.append({
                "status": "Server is up.",
                "server_name": info.server_name,
                "game": info.game,
                "map": info.map_name,
                "server_address": address[0],
                "server_port": info.port,
                "players": info.player_count,
                "max_players": info.max_players,
        })

        return servers