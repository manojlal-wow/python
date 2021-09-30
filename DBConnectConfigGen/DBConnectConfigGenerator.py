import datetime
import os
import csv


def main():
    print("Processing Start Time:" + datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)") + "\n")
    print("""Please choose the db connect config file template to proceed:

             1. db_inputs.conf
             
             2. db_connections.conf
             
             3. Both 1 & 2""")
    template_option = input()
    if template_option != "1" and template_option != "2" and template_option != "3":
        print("""Invalid Option Selected !!!!
                 Please rerun the script and enter a valid Option.""")
        exit()
    cwd = os.getcwd()
    pathsep = os.path.sep
    template_file = cwd + pathsep + "templates" + pathsep + "db_inputs_template.txt"
    output_file = "db_inputs.txt"
    template_list = []
    
    if template_option == "1":
        template_list.append("1")
    elif template_option == "2":
        template_list.append("2")
    elif template_option == "3":
        template_list.append("1")
        template_list.append("2")
        
    data_file = cwd + pathsep + "data" + pathsep + "dbcon_data.csv"
    output_dir = cwd + pathsep + "output" + pathsep
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for x in template_list:
        if x == "1":            
            template_file = cwd + pathsep + "templates" + pathsep + "db_inputs_template.txt"
            output_file = "db_inputs.txt"
        if x == "2":
            template_file = cwd + pathsep + "templates" + pathsep + "db_connections_template.txt"
            output_file = "db_connections.txt"
            
        with open(output_dir + output_file, 'w+', encoding='ISO-8859-1') as file_output:
            with open(template_file, 'r', encoding='ISO-8859-1') as input_file:
                content = input_file.read()
                with open(data_file, 'r', encoding='ISO-8859-1') as csv_data:
                    reader = csv.DictReader(csv_data)
                    for row in reader:
                        host_val = row['host']
                        db_val = row['db']
                        conn_prefix = row['connection_prefix']
                        result = content.replace("<host>", host_val).replace("<db>", db_val).replace("<connection_prefix>", conn_prefix).join("\r\n")
                        if x == "1":
                            index = row['index']
                            result = result.replace("<index>", index)
                        if x == "2":
                            identity = row['identity']
                            result = result.replace("<identity>", identity)
                        
                        file_output.write(result)                
    
    print("Processing End Time:" + datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))

if __name__ == '__main__':
    # execute only if run as a script
    main()
