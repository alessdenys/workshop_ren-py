define a = Character('Aless', color="#808080")
define b = Character('Belinda', color="#8B0000")
label start:
    scene eclipse with fade
    show aless at left with dissolve 
    a "Bonjours à tous, notre workshop portera sur ren'py et sur la place du python dans ce dernier!"
    a "Alors pour le python je suppose qu'avec les 3 workshops qui lui étaient consacrés, vous savez déjà en gros ce que c'est donc, nous n'allons pas vous faire l'affront de vous le réexpliquer mais nous parlerons plus tard de son intégration dans ren'py. "
    a "Nous allons donc d'abord expliquer ce qu'est ren'py, ce dernier étant moins connu."
    a "ren'py est un moteur de jeux axé sur la création de visual novels mais permettant en réalité de créer un bon nombre de jeux vidéos avec des méchaniques diverses et variées (en théorie il est même possible de créer des rpg comme sur rpg maker). "
    a "ren'py est extrêment puissant pour une simple raison, il est conçu pour fonctionner avec le langage python."
    show belinda at right with dissolve 
    hide aless
    b "Nous avons parlé de visual novels mais qu'est ce que c'est? Et bien ce sont des \"romans visuels\" la forme la plus basique étant une succession d'images et de textes (on appelle cela un kinetic novel)." 
    b "Toutefois, la majorité des VN rajoutes une notion de choix afin de rendre leur histoire plus interactives. Il y a aussi de plus en plus de visual novels qui reprennent des éléments de jeux de gestion, voir qui en deviennent eux même."
    b "Aussi, quelque chose d'agréable avec ren'py c'est qu'il y a une assez bonne communauté et qu'on peut facilement trouver des ressources mises à disposition \"gratuitement\" par les gens."
    b "notamment des images, des sprites voir des musiques ou même des transitions, des styles d'affichage pour le menu, des boutons... "
    b "Maintenant que ces éléments importants sont introduits, si personne n'a de question, nous allons passer à quelque chose de plus concret en créant ensemble un VN et en voyant un peu mieux le rôle de python et une partie de son potentiel."