# def title_case(title, minor_words=''):
#     excluded_words = [word.lower() for word in minor_words.split(' ')]
#     title_words = [word.lower() for word in title.split(' ')]

#     for i in range(len(title_words)):
#     	if title_words[i] not in excluded_words or i == 0:
#     		title_words[i] = title_words[i][0].upper() + title_words[i][1:]

#     return (' ').join(title_words)



# Best solution
def title_case(title, minor_words=''):
	title= title.capitalize().split()
	minor_words = minor_words.lower().split()
	return ' '.join([word if word in minor_words else word.capitalize() for word in title])


print(title_case('a clash of Kings', 'a an the of'))