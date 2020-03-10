label miam_miam:
    l "J'adore vraiment le chocolat!"
    hide alien-chocolat with dissolve
    $fatigue = 0
    l "Maintenant je vais vous montrer comment faire une boucle"
    while fatigue < 3:
        $sale = True
        $bois = False
        $sleep = False
        while sleep == False:
            menu:
                l "Que faire maintenant?"
                "nettoyer l'endroit" if sale == True:
                    $fatigue += 1
                    l "Ouf! enfin propre!"
                    $sale = False
                "allez chercher du bois" if bois == False:
                    $fatigue += 1
                    l "avec ça on devrait pouvoir faire un bon feu!"
                    $bois = True
                "me reposer":
                    if fatigue < 3:
                        $fatigue = 0
                    l "yaaawn. c'était une longue journée"
                    $sleep = True
                "lire un livre":
                    $fatigue += 1
                    l "Level 26? ça à l'air intéressant"
    l "Et maintenant à vous de jouer!"
            
    stop sound
    return