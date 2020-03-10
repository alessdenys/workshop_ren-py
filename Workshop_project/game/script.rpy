# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define l = Character('Luna', color="#c88fc8")

label start:
    scene black
    "???" "Bonjour Becode, je vais vous montrer comment créer un visual novel en ren'py"

    "???" "Si tout va bien, vous devriez déja savoir ce qu'est un visual novel et ce qu'est ren'py, nous allons donc commencer directement!"

    "???" "Déja je vais vous montrer comment définir un personnage, ce sera plus pratique pour se parler."

    "???" "Première étape, au dessus de \"label start\", rajouter \"define l = Character('Luna', color=\"#c88fc8\")\""
    l "Ha c'est quand même mieux d'avoir un nom! Bon la prochaine fois vous pourrez personnaliser le nom ainsi que la couleur bien entendu."
    
    l "Bien, passons à la deuxieme étape, vous allez définir une image, je vous montre comment ci-dessous!"

    show base_luna at left

    l "Après avoir appellé une image ou une scene, il faut toujours rajouter du texte sinon ren'py renverra directement au menu principal."
    
    l "Maintenant allumons la lumière!"

    scene beach_night
    l "Voila c'est mieux!"

    l "Bien mais c'est un peu triste ici, je vais vous montrer comment mettre un peu d'ambiance mais aussi comment faire un menu"

    menu:
        l "vas-tu mettre : "
        "Beach":
            play sound "sons/beach.mp3"
        "Do It":
            play sound "sons/do_it.wav"
    l "C'est quand même plus agréable avec de la musique!"

    l "C'est bien beau tout ça mais si je veux personnaliser l'experience pour chacun comment faire en sorte que les choix aient un réel impact? excellente question billy!"
    l "C'est très simple il suffit de déclarer une variable comme ci-dessous"
    $aime_le_chocolat = False
    l "Alors ici j'ai créé un booléen mais on aurait pu faire n'importe quelle variable python par exemple un integer :"
    $poid = 60
    l "Maintenant on a nos variables mais elles ne servent encore à rien je vais donc vous montrer comment les faire varier et comment leurs donner un impact"

    menu:
        "j'aime le chocolat":
            $aime_le_chocolat = True
        "Beurk je préfère le gras":
            $poid += 10
    l "Voici comment les modifier, c'est assez simple. Et maintenant je vais vous montrer comment les utiliser"

    menu: 
        l "je vais :"
        "manger du chocolat" if aime_le_chocolat == True:
            l "Chocoolaat!"
        "faire régime" if poid > 60:
            l "j'ai un peu exagéré avec la mayonnaise"
    l "Donc on peut masquer ou afficher des options selon les choix précédant mais on peut aussi changer l'issue d'un choix! (je vais aussi en profiter pour parler des labels et des jumps)"

    menu:
        l "Ho mon dieu un monstre de chocolat que faire?!"
        "le manger":
            if aime_le_chocolat == True:
                jump miam_miam
            else:
                jump LA_MORT
        "Fuir":
            if poid < 61:
                l "Je crois que je l'ai semé"
            else:
                l "C'est trop dur de courir, j'aurais vraiment du mieux manger!"
    ###Et maintenant on termine ce label et on définit les labels pour les jumps (oui on les définit après le jump) 
    ###On va aussi en définir dans un autre fichier pour montrer avec quelle facilité on peut fractionner notre tavail
    stop sound
    return 
    with fade
label LA_MORT:
    l "Beurk j'aime vraiment pas le chocolat!{w} mais qu'est ce qu'il fait?! Haaaa il me mange! Haaaa!"

    stop sound
    return  