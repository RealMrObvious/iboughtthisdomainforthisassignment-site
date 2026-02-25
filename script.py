import random

folder = './adv'
num_sites = 500
site_content_template = """
            <!DOCTYPE html>
            <html>
            <body>

            <header_goes_here>
            <links_go_here>

            </body>
            </html>
            """


for i in range(num_sites):
    site_content = site_content_template
    num_outgoing_links = random.randint(1,10)
    outgoing_links =  random.sample(range(0,num_sites), num_outgoing_links)
    links_to_add = ''

    for num in outgoing_links:
        if(folder == './adv'):
            if(num != i): # dont link to self
                links_to_add += f'<a href="N_{i+1}.html">N_{num} </a>'

        elif(folder == './basic'):
            plus1 = i + 1
            minus1 = i - 1

            if(plus1 > num_sites - 1):
                plus1 = 0
            
            if(minus1 < 0):
                minus1 = num_sites

            links_to_add = f'<a href="N_{minus1}.html">N_{minus1} </a> <a href="N_{plus1}.html">N_{plus1} </a>'


    site_content = site_content.replace("<links_go_here>",links_to_add)
    site_content = site_content.replace("<header_goes_here>",f"<h1> Welcome to N_{i}</h1>")

    with open(f'{folder}/N_{i}.html','w') as site:
        site.writelines(site_content)
    
    # if u need to verify where the links go
    if(folder == './adv'):
        with open(f'outgoinglinks.txt','a+') as adj_graph:
            adj_graph.write(f"N_{i}  links to:  {outgoing_links}\n")
