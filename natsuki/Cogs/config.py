class conf():

    token = "token"
    prefix1 = "satania_"
    prefix2 = "Satania_"
    name = "Satania"
    cogd = "Cogs"
    type_speed = 2
    playing_msg = ["Type 'satania_help' for help!", "El Diablo", "pranks on Gab", "with Dog", "Hide and Seek with her melon pan"]
    admins = [360630210372304898, 356262707717996545, 492446848246611969]
    #         Winston             Daniel              Angelo 
    test_mode = True  #To enable this function, use any value that is NOT "False" Otherwise you would be disabling this function

    if test_mode is False:
        sharding = True
        version = "1.0G Skittles"
    else:
        sharding = False
        version = "1.OG Skittles" # Testing mode should be beta.
    #L|Launch    B|Beta

    ''' Just wanted to clear out that these hex codes bellow are for embed colours so i don't have to keep changing them in every single fucking file '''
    err = 0xC91313 # The Error Embed Colour
    norm = 0xff4242 # The Normal or Yeah sure i did this command heres an embed color Embed Colour
    warn = 0xff42e2 # The Warning Embed Colour
    suc = 0xff42e2 # The Success i did a thing Embed Colour

    ''' These are just some error quotes so i can change them really quickly instead of doing the same quote for each error in every file '''
    everyone_tag = "Are you some sort of demon, trying to ping everyone?"

    ''' These are for the chat trigger''' 
    w_tog_on = []

    ''' Doki Bot's ID'S '''
    if test_mode is True or test_mode is 1:
        natsuki_id = 669783536852795412
        monika_id = 669404759207313419 
        sayori_id = 669788780726583299
        yuri_id = 669788418510684201
        mc_id = 669790111969443840

    else: 
        natsuki_id = 669783536852795412
        monika_id = 669404759207313419 
        sayori_id = 669788780726583299
        yuri_id = 669788418510684201
        mc_id = 669790111969443840


