import re
def domain_name(url):
    domainRegex = re.compile(r'(https://www\.|http://www\.|http://|https://|www\.)?([\w-]*)(\..*)')
    if domainRegex.match != None:
        return domainRegex.match(url).groups()[1]

print(domain_name('https://hyphen-site.org'))