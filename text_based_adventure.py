# Pre-Adventure Questions
name = input("Hello adventurer, what is your name?:\n ")
print("Greetings, " + name + ". Are you ready to go on a quest?")
answer = input("yes/no:\n")

if answer.lower().strip() == "yes":

    answer = input("You awake in a haze, it appears you are in a dimly lit dungeon in a small cell. Do you scream for help or wait? (scream / wait)\n ").lower().strip()
    
    if answer == "scream":
        
        answer = input("Your voice echos down the dark and empty corridor.  You wait for some time before hearing... nothing.  It appears as if this dungeon is abandoned. Do you attempt to escape or wallow and cry (escape/cry)\n ")

        if answer == "escape":

            answer = input("You look around the cell, the cobblestone floor is covered with gravel and hay with rocks in one corner of the cell, the walls are dull, and the cell doors are sturdy, yet rusted. Inspect the rocks or the bars (rocks/bars)?\n ")

            if answer == "rocks":
               
                answer = input("You move the rocks to the side.  After all have been moved, you can see that crudely placed wooden planks were being hidden by the rocks.  Try to kick in the boards or lift them? (kick/lift)\n ") 
               
                if answer == "kick":

                    answer = input("You kick in the center of all the boards, and to a great surprise they almost immediately cave in giving way to first your foot then your leg.  You catch yourself on the only board left... whew... SNAP!  You drop down a dark hole and hit the ground, water splashing all around you.  You stand and can see in the dim light that you're standing in horrible smelling, knee-high water.  Must be an old ratway, there is light coming from the end of the tunnel, go towards it (yes/no)\n ")

                    if answer == "yes":
                          
                        answer = input("You wade in the murky water towards the dim light at the end of the tunnel.  Rats and bugs crawl around you on the edges of the wall... but they're going away from you, hmm.  Upon walking for a few more minutes you hear a strange sound, like... squishing?  Suddenly a person sized collective of a dark green slime emerges from the water. He looks as if he is about to attack!  (punch/kick)\n  ")

                        if answer == "punch":
    
                            answer = input("You swing your arm wildly at the slime.  Your fist squishes into the slime until a great pressure releases allowing your hand to travel clean through part of the slime.  Chunks of slime splatter onto the sewer wall as the slime stumbles and rolls back before using all its force to make another lunge at you. Punch again or run? (punch/run)\n  ")

                            if answer == "punch":

                                answer = input("You take another swing at it but this time your hand lands in its chest... but the slime tightens around your arm.  It pulls you down under the water and surrounds your body, it kills you in a matter of minutes. Wrong move " + name + ".  GAME OVER\n")

                            elif answer == "run":

                                answer = input("You just barely dodge the slime as its gelatenous body sinks back into the water behind you.  You run towards the light.  After a minute of running you reach the end and bow your head to catch your breath.  You look up to see that the end of the ratway opens up to a forest.  You step out into the fresh midday air and try to decide what the best idea is from here... sit under a tree or keep running forwards into the forest? (sit/forward)\n ")

                                if answer == "sit":

                                    answer = input("You sit under a tall tree and relax.%%%%%%%%%%%%%%%%%%%%%%%%%%%")

                                elif answer == "forward":

                                    answer = input("You run forward into the forest.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
 
                        elif answer == "kick":

                            answer = input("You swing your foot into the side of the slime.  But instead of hurting it, your foot just sticks in it.  As you hop around the slime moves forward quickly taking you into the water with it.  The slime drowns you.  GAME OVER.  ")

                    elif answer == "no":

                        answer = print("You turn and walk into the dark, after some time, you hear a growl... before you have time to think... SNAP!  GAME OVER")

                elif answer == "lift":

                    answer = input("You lift up the rotted boards rather easily.  Inside it is dark but you can feel a breeze, must be a way out... you drop down into knee high water and can see light in front of you... unless you want to go backwards? (forward/backward)\n ")

                    if answer == "forward":
                          
                        answer = input("You wade in the murky water towards the dim light at the end of the tunnel.  Rats and bugs crawl around you on the edges of the wall... but they're going away from you, hmm.  Upon walking for a few more minutes you hear a strange sound, like... squishing?  Suddenly a person sized collective of a dark green slime emerges from the water. He looks as if he is about to attack!  (punch/kick)\n  ")

                        if answer == "punch":
    
                            answer = input("You swing your arm wildly at the slime.  Your fist squishes into the slime until a great pressure releases allowing your hand to travel clean through part of the slime.  Chunks of slime splatter onto the sewer wall as the slime stumbles and rolls back before using all its force to make another lunge at you. Punch again or run? (punch/run)\n  ")

                            if answer == "punch":

                                answer = input("You take another swing at it but this time your hand lands in its chest... but the slime tightens around your arm.  It pulls you down under the water and surrounds your body, it kills you in a matter of minutes. Wrong move " + name + ".  GAME OVER\n")

                            elif answer == "run":

                                answer = input("You just barely dodge the slime as its gelatenous body sinks back into the water behind you.  You run towards the light.  After a minute of running you reach the end and bow your head to catch your breath.  You look up to see that the end of the ratway opens up to a forest.  You step out into the fresh midday air and try to decide what the best idea is from here... sit under a tree or keep running forwards into the forest? (sit/forward)\n ")
 
                        elif answer == "kick":

                            answer = input("You swing your foot into the side of the slime.  But instead of hurting it, your foot just sticks in it.  As you hop around the slime moves forward quickly taking you into the water with it.  The slime drowns you.  GAME OVER.  ")

                    elif answer == "backward":

                        answer = print("You turn and walk into the dark, after some time, you hear a growl... before you have time to think... SNAP!  GAME OVER")

            elif answer == "bars":
               
                answer = input("You move your way to the bars, upon quick inspection it appears that the bars have a door with a rusted lock.  May be able to get it open... with a kick or maybe with your shoulder... (kick, shoulder)\n ") 
                   
                if answer == "shoulder":
           
                    answer = input("You march back to the end of the cell, and with your breath held, you run full force at the door.  Upon impact with the door you trip on a ledge and fly through the door... it appears it has been open the entire time.  You stand and brush yourself off, you've made it out of the cell.  Do you go left or right down the hallway? (left/right)\n  ")                          

                    if answer == "left":
    
                        answer = input("You run left down the dim hallway.  At the end of the hallway theres a doorway emiiting some light.  Upon entering you see a long set of stairs and at the end a group of multiple hooded figures standing in a circle around a crude drawing carved into the floor.  You walk down a few steps but your foot hits something... a sword!  You hold the sword, do you run or inspect more? (run/inspect)\n  ")

                        if answer == "inspect":
 
                            answer = input("You walk down the stairs slowly to avoid being noticed, you make it to the end and hide behind a pillar.  Do you wait and watch or do you attack them? (hide/attack)  ")

                            if answer == "attack":

                                answer = input("You ready the sword in your hand and lunge out from your position towards one of the hooded figures.  Your sword swings killing the person instantly, the other hooded figures take notice. 'GET THEM' they yell, attack the person to your left or right? (left/right)\n ")
                               
                                if answer == "left":

                                    answer = input("You stab to your left as a man screams 'NOOOOO' and collapses to the ground, do you look at the others and take a large swing or try another stab at an individual? (swing/stab)\n  ")
                                
                                elif answer == "right":

                                    print("You take a slash to your left but miss, you look up but it is too late, the rest of the cultists stab you to death.  GAME OVER")                               

                        elif answer == "run":
     
                            answer = input("You turn to run but trip on a stair.  You tumble down the flight of stairs...  upon reaching the end the hooded figures yell 'THE SACRIFICE, GET THEM'.  The sword is nowhere in sight.  Run or fight with fists (run/fight)  ")

                            if answer == "fight":

                                answer = input("  ")

                    elif answer == "right":

                        answer = input("YOU RUN TO THE RIGHT!!!!!!  ")

                elif answer == "kick":
 
                     answer = input("You kick the door and it immediately swings open... oh.. it was unlocked.  Go left or right down the hallway? (left/right)\n  ")

                     if answer == "left":
    
                        answer = input("You run left down the dim hallway.  At the end of the hallway theres a doorway emiiting some light.  Upon entering you see a long set of stairs and at the end a group of multiple hooded figures standing in a circle around a crude drawing carved into the floor.  You walk down a few steps but your foot hits something... a sword!  You hold the sword, do you run or inspect more? (run/inspect)\n  ")

                        if answer == "inspect":
 
                            answer = input("You walk down the stairs slowly to avoid being noticed, you make it to the end and hide behind a pillar.  Do you wait and watch or do you attack them? (hide/attack)  ")

                            if answer == "attack":

                                answer = input("You ready the sword in your hand and lunge out from your position towards one of the hooded figures.  Your sword swings killing the person instantly, the other hooded figures take notice. 'GET THEM' they yell, attack the person to your left or right? (left/right)\n ")
                               
                                if answer == "left":

                                    answer = input("You stab to your left as a man screams 'NOOOOO' and collapses to the ground, do you look at the others and take a large swing or try another stab at an individual? (swing/stab)\n  ")
                                
                                elif answer == "right":

                                    print("You take a slash to your left but miss, you look up but it is too late, the rest of the cultists stab you to death.  GAME OVER")                               

                        elif answer == "run":
     
                            answer = input("You turn to run but trip on a stair.  You tumble down the flight of stairs...  upon reaching the end the hooded figures yell 'THE SACRIFICE, GET THEM'.  The sword is nowhere in sight.  Run or fight with fists (run/fight)  ")

                            if answer == "fight":

                                answer = input("With your fists up you take wild swings at the various foes.  Your head is quickly covered with a sack, and after some struggling, they knock you out...  You wake up chained to the wall in front of the carving in the ground %%%%%%%%%%%%% ")

                     elif answer == "right":

                        answer = input("YOU RUN TO THE RIGHT!!!!!!  ")


        elif answer == "cry":
           
            print("You cry and cry and cry...no one comes for you. " + name + "  dies starving and alone...  GAME OVER")
  
    elif answer == "wait":

         answer = input("You wait and wait, with no sunlight it is impossible to know how many days have passed.  After what feels like forever, you decide you should either wait for longer or try and escape (wait / escape)\n ")

         if answer == "wait":
             
             answer = print("The borden of the cell eats away at your mind.  " + name + ", " + name + ", " + name + "... come to the light.  Starving and tired, you close your eyes and die.  GAME OVER.")

         elif answer == "escape":

            answer = input("You look around the cell, the cobblestone floor is covered with gravel and hay with rocks in one corner of the cell, the walls are dull, and the cell doors are sturdy, yet rusted. Inspect the rocks or the bars (rocks/bars)?\n ")

            if answer == "rocks":
               
                answer = input("You move the rocks to the side.  After all have been moved, you can see that crudely placed wooden planks were being hidden by the rocks.  Try to kick in the boards or lift them? (kick/lift)\n ") 
               
                if answer == "kick":

                    answer = input("You kick in the center of all the boards, and to a great surprise they almost immediately cave in giving way to first your foot then your leg.  You catch yourself on the only board left... whew... SNAP!  You drop down a dark hole and hit the ground, water splashing all around you.  You stand and can see in the dim light that you're standing in horrible smelling, knee-high water.  Must be an old ratway, there is light coming from the end of the tunnel, go towards it (yes/no)\n  ")
                       
                    if answer == "yes":
                          
                        answer = input("You wade in the murky water towards the dim light at the end of the tunnel.  Rats and bugs crawl around you on the edges of the wall... but they're going away from you, hmm.  Upon walking for a few more minutes you hear a strange sound, like... squishing?  Suddenly a person sized collective of a dark green slime emerges from the water. He looks as if he is about to attack!  (punch/kick)\n  ")

                        if answer == "punch":
    
                            answer = input("You swing your arm wildly at the slime.  Your fist squishes into the slime until a great pressure releases allowing your hand to travel clean through part of the slime.  Chunks of slime splatter onto the sewer wall as the slime stumbles and rolls back before using all its force to make another lunge at you. Punch again or run? (punch/run)\n  ")

                            if answer == "punch":

                                answer = input("You take another swing at it but this time your hand lands in its chest... but the slime tightens around your arm.  It pulls you down under the water and surrounds your body, it kills you in a matter of minutes. Wrong move " + name + ".  GAME OVER\n")

                            elif answer == "run":

                                answer = input("You just barely dodge the slime as its gelatenous body sinks back into the water behind you.  You run towards the light.  After a minute of running you reach the end and bow your head to catch your breath.  You look up to see that the end of the ratway opens up to a forest.  You step out into the fresh midday air and try to decide what the best idea is from here... sit under a tree or keep running forwards into the forest? (sit/forward)\n ")
 
                        elif answer == "kick":

                            answer = input("You swing your foot into the side of the slime.  But instead of hurting it, your foot just sticks in it.  As you hop around the slime moves forward quickly taking you into the water with it.  The slime drowns you.  GAME OVER.  ")

                    elif answer == "no":

                        answer = print("You turn and walk into the dark, after some time, you hear a growl... before you have time to think... SNAP!  GAME OVER")
      
                elif answer == "lift":

                    answer = input("You lift up the rotted boards rather easily.  Inside it is dark but you can feel a breeze, must be a way out... you drop down into knee high water and can see light in front of you... unless you want to go backwards? (forward/backward)\n ")

                    if answer == "forward":
                          
                        answer = input("You wade in the murky water towards the dim light at the end of the tunnel.  Rats and bugs crawl around you on the edges of the wall... but they're going away from you, hmm.  Upon walking for a few more minutes you hear a strange sound, like... squishing?  Suddenly a person sized collective of a dark green slime emerges from the water. He looks as if he is about to attack!  (punch/kick)\n  ")

                        if answer == "punch":
    
                            answer = input("You swing your arm wildly at the slime.  Your fist squishes into the slime until a great pressure releases allowing your hand to travel clean through part of the slime.  Chunks of slime splatter onto the sewer wall as the slime stumbles and rolls back before using all its force to make another lunge at you. Punch again or run? (punch/run)\n  ")

                            if answer == "punch":

                                answer = input("You take another swing at it but this time your hand lands in its chest... but the slime tightens around your arm.  It pulls you down under the water and surrounds your body, it kills you in a matter of minutes. Wrong move " + name + ".  GAME OVER\n")

                            elif answer == "run":

                                answer = input("You just barely dodge the slime as its gelatenous body sinks back into the water behind you.  You run towards the light.  After a minute of running you reach the end and bow your head to catch your breath.  You look up to see that the end of the ratway opens up to a forest.  You step out into the fresh midday air and try to decide what the best idea is from here... sit under a tree or keep running forwards into the forest? (sit/forward)\n ")
 
                        elif answer == "kick":

                            answer = input("You swing your foot into the side of the slime.  But instead of hurting it, your foot just sticks in it.  As you hop around the slime moves forward quickly taking you into the water with it.  The slime drowns you.  GAME OVER.  ")

                    elif answer == "backward":

                        answer = print("You turn and walk into the dark, after some time, you hear a growl... before you have time to think... SNAP!  GAME OVER")


            elif answer == "bars":
               
                answer = input("You move your way to the bars, upon quick inspection it appears that the bars have a door with a rusted lock.  May be able to get it open... with a kick or maybe with your shoulder... (kick, shoulder)\n ") 
                   
                if answer == "shoulder":
           
                    answer = input("You march back to the end of the cell, and with your breath held, you run full force at the door.  Upon impact with the door you trip on a ledge and fly through the door... it appears it has been open the entire time.  You stand and brush yourself off, you've made it out of the cell.  Do you go left or right down the hallway? (left/right)\n  ")                          

                    if answer == "left":
    
                        answer = input("You run left down the dim hallway.  At the end of the hallway theres a doorway emiiting some light.  Upon entering you see a long set of stairs and at the end a group of multiple hooded figures standing in a circle around a crude drawing carved into the floor.  You walk down a few steps but your foot hits something... a sword!  You hold the sword, do you run or inspect more? (run/inspect)\n  ")

                        if answer == "inspect":
 
                            answer = input("You walk down the stairs slowly to avoid being noticed, you make it to the end and hide behind a pillar.  Do you wait and watch or do you attack them? (hide/attack)  ")

                            if answer == "attack":

                                answer = input("You ready the sword in your hand and lunge out from your position towards one of the hooded figures.  Your sword swings killing the person instantly, the other hooded figures take notice. 'GET THEM' they yell, attack the person to your left or right? (left/right)\n ")
                               
                                if answer == "left":

                                    answer = input("You stab to your left as a man screams 'NOOOOO' and collapses to the ground, do you look at the others and take a large swing or try another stab at an individual? (swing/stab)\n  ")
                                
                                elif answer == "right":

                                    print("You take a slash to your left but miss, you look up but it is too late, the rest of the cultists stab you to death.  GAME OVER")                               

                        elif answer == "run":
     
                            answer = input("You turn to run but trip on a stair.  You tumble down the flight of stairs...  upon reaching the end the hooded figures yell 'THE SACRIFICE, GET THEM'.  The sword is nowhere in sight.  Run or fight with fists (run/fight)  ")

                            if answer == "fight":

                                answer = input("  ")

                    elif answer == "right":

                        answer = input("YOU RUN TO THE RIGHT!!!!!!  ")

                elif answer == "kick":
 
                     answer = input("You kick the door and it immediately swings open... oh.. it was unlocked.  Go left or right down the hallway? (left/right)\n  ")

                     if answer == "left":
    
                        answer = input("You run left down the dim hallway.  At the end of the hallway theres a doorway emiiting some light.  Upon entering you see a long set of stairs and at the end a group of multiple hooded figures standing in a circle around a crude drawing carved into the floor.  You walk down a few steps but your foot hits something... a sword!  You hold the sword, do you run or inspect more? (run/inspect)\n  ")

                        if answer == "inspect":
 
                            answer = input("You walk down the stairs slowly to avoid being noticed, you make it to the end and hide behind a pillar.  Do you wait and watch or do you attack them? (hide/attack)  ")

                            if answer == "attack":

                                answer = input("You ready the sword in your hand and lunge out from your position towards one of the hooded figures.  Your sword swings killing the person instantly, the other hooded figures take notice. 'GET THEM' they yell, attack the person to your left or right? (left/right)\n ")
                               
                                if answer == "left":

                                    answer = input("You stab to your left as a man screams 'NOOOOO' and collapses to the ground, do you look at the others and take a large swing at the group or try another stab at an individual? (swing/stab)\n  ")

                                    if answer == "swing":

                                        answer = input("You quickly bring your sword up and slash towards the remaining cultists, cutting one down instantly, and staggering the others, some of which are beginning to flee... attempt to kill the remaining or hold one captive with your sword at their neck? (kill/captive)\n ")

                                        if answer == "kill":

                                            answer = input("You cut down the remaining cultists%%%%%%%%%%% ")

                                    elif answer == "stab":

                                        print("You take a stab at the cultist to your left, but upon looking up you see it is too late, the rest of the cultists stab you to death.  GAME OVER ")
                                
                                elif answer == "right":

                                    print("You take a slash to your left but miss, you look up but it is too late, the rest of the cultists stab you to death.  GAME OVER")                               

                        elif answer == "run":
     
                            answer = input("You turn to run but trip on a stair.  You tumble down the flight of stairs...  upon reaching the end the hooded figures yell 'THE SACRIFICE, GET THEM'.  The sword is nowhere in sight.  Run or fight with fists (run/fight)  ")

                            if answer == "fight":

                                answer = input("  ")

                     elif answer == "right":

                        answer = input("YOU RUN TO THE RIGHT!!!!!!  ")


else:
   
    print("That is too bad")
