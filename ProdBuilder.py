class PageProdBuilder():
    
    def __init__(self,dev_file_path,prod_file_path):
        self.__dev_file_path = dev_file_path
        self.__prod_file_path = prod_file_path
        
    def build(self):
        __dev_file = open(self.__dev_file_path, "rt")
        __prod_file = open(self.__prod_file_path, "w")
    
        __dev_html = __dev_file.read()
        
        __prod_html = ''
    
        for i in range(len(__dev_html)):
            if __dev_html[i] == '\n':
                continue
            else:
                __prod_html = __prod_html + __dev_html[i]         
            
            
        __prod_file.write(__prod_html)
    
        __dev_file.close()
        __prod_file.close()
