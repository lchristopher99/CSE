'''
This is the skeleton sorce code of your final exam. Please write your solution here.

Write your name : Logan Christopher

Write your netid : CLC1085  

Please try to use the given function skeletons.

Best of luck!!!
'''
import pickle

# main function. 
def main ():
  emails = None

  try:
    emails = open('email_addresses.txt')
  except Exception:
    print('Error has occured within main().')

  email_list = get_email_list(emails)
  
  localDomain = get_localDomain_list(email_list)

  unique_emails = strip_emails(localDomain)

  pickle_list(unique_emails)

  print ("Process of pickling unique emails complete. Please check working directory for pickled data.")

# function to open the input file and create a list of email addresses.
def get_email_list(emails):
  email_list = []
  if emails != None:
    for line in emails:
      email_list.append(line)
  else:
    print('Error has occured within get_email_list().')

  if emails != None:
    return email_list


# function to get the local name part of the email address
def get_localDomain_list(email_list):
  localDomain_names = []

  for emails in email_list:
    localDomain_names.append(emails.split('@'))
  
  return localDomain_names

# function to compare two local names
def strip_emails(localDomain):
  unique_email_list = []

  for el in localDomain:
    email = el[0].replace('.','') + '@' + el[1]
    unique_email_list.append(email)
  
  seen = set()
  unique_emails = []
  for el in unique_email_list:
    if el not in seen:
      seen.add(el)
      unique_emails.append(el)
  
  return unique_emails

# function to pickle the list of unique emails
def pickle_list(unique_emails):
  pickled_data = open('pickled_unique_email_list.dat', 'wb')
  pickle.dump(unique_emails, pickled_data)
  pickled_data.close()


if __name__ == '__main__':
  main()
