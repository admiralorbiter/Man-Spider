define s = Character("Man Spider")

label start:
    transform fullscreen_image:
        size (1920, 1080)
        truecenter

    show man spider at fullscreen_image
    "About a Spider, who wants to be a "
    "...man."

    show 1 at fullscreen_image
    "But no matter how hard he tried, society wouldn't accept him."
    show 2 at fullscreen_image  
    "But he was denied a car loan..."
    show 3 at fullscreen_image
    "Then a house loan..."
    show 5 at fullscreen_image
    "Finally, he was fired from his data entry job because he was outed by his coworkers"
    show 4 at fullscreen_image
    "He was left low and with only one option"
    show 6 at fullscreen_image
    "A new beginning"
    jump choice2

label choice1:
    "I choose the lottery"

label choice2:
    "I choose spiders"

