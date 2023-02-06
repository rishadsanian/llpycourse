#List of stories Directory for Mad Lib Game. 

#Intro
mainscreen="""

░░░░░░╔═╦═╦══╦══╗╔╗╔══╦══╦══╗░░░░░░
░░░░░░║║║║║╔╗╠╗╗║║║╚║║╣╔╗║══╣░░░░░░
░░░░░░║║║║║╠╣╠╩╝║║╚╦║║╣╔╗╠══║░░░░░░
░░░░░░╚╩═╩╩╝╚╩══╝╚═╩══╩══╩══╝░░░░░░
      MAD LIBS GAME by RISHAD 
            
      Choose your story type:

       type 0 for COLDPLAY
       type 1 for NURSERY RYHME
       type 2 for QUOTE
       type 3 to EXIT
                           """

            

print(mainscreen)
          
#stories and prompts 
storytext=""
storytitle=""
storyprompt=""

story1=[
  "Coldplay","VERB at the NOUN. Look how they VERB for you, and everything you do. Yeah, they were all DESCRIPTION.", #Title and Story 
  [["a verb: ","VERB"],["a noun:","NOUN"],["a verb:","VERB"],["a descritive word:", 'DESCRIPTION']] #Prompt and Placeholders
]
story2=[
  "Nursery Rhyme","There was a PROFESSION, who had a NOUN, and ADJECTIVE was his NOUN O!", 
  [["a profession:","PROFESSION"],["a noun:","NOUN"], ["an adjective: ","ADJECTIVE"], ["a noun:","NOUN"]]  
]
story3=[
  "Quote", "Behind every ADJECTIVE NOUN, is a INGADJECTIVE NOUN.", 
  [["a noun","NOUN"], ["an adjective", "ADJECTIVE"],["an adjective ending with ing","INGADJECTIVE"],["a noun", "NOUN"]]
]

stories=[story1, story2, story3] #story database

#PROMPT SEQUENCE PICK STORY
i=0
userstoryselect=""

#User input and numerical validation
while i==0: #Infinite loop
  while True:
    try:
      userstoryselect=int(input("Type 0,1,or 2 to load story:\n Press 3 to exit.")) #Prompt-Story selector and int validation
      break
    except ValueError:
        print("Oops! That was not a valid number. Try again.")

#Exit option          
  if userstoryselect==3:
    print("Goodbye!")
    break

#Numerical range validation
  elif userstoryselect>2 :
    print("Invalid entry, please try again.")

#Game computation
  else:       
      storysel=stories[userstoryselect]
      storytitle = storysel[0]
      storytext = storysel[1]
      storyprompt = storysel[2]
      for prompt, placeholder in storyprompt:
        userinput=input("Please enter "+ prompt) #Prompt word input
        storytext=storytext.replace(placeholder,userinput,1)

#Output
  if storyprompt != "":
      print ("\nYou chose "+storytitle+".\n\n"+storytext)
      print ("\n\nSelect another or type 3 to exit.\n")

#reset
storytext=""
storytitle=""
storyprompt=""