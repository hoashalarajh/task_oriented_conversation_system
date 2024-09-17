from hstn import hstn

# creating an object of hstn class
dialogue_system = hstn()

# storing the text1 in about_lecture method and others for building the diaogue system
dialogue_system.about_lecture = text1
dialogue_system.clarity = text4
dialogue_system.student_interaction = text3
dialogue_system.task_organization = text2

# running the overall system
dialogue_system.run_system_A()