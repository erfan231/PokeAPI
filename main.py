from tkinter import *
import requests
import list_pokeapi


def main_func():
    try:
        users_id = int(get_id.get())
        
        if users_id > 898:
            pokemon_name.config(text=f"Enter a valid ID (lower than 899)")
            default_img = requests.get("https://www.iconsdb.com/icons/preview/white/square-xxl.png")
            default_img_data = default_img.content

            img = PhotoImage(data=default_img_data)
            image.configure(image=img)
            image.image = img

        else:
            image_url = requests.get(
                f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{users_id}.png")
            image_data = image_url.content

            img = PhotoImage(data=image_data)
            image.configure(image=img)
            image.image = img
            pokemon_name.config(text=f"Pokemon Name: {list_pokeapi.data_list[users_id]}")

    except ValueError:
        pokemon_name.config(text=f"Enter a valid ID (digit only)")
        default_img = requests.get("https://www.iconsdb.com/icons/preview/white/square-xxl.png")
        default_img_data = default_img.content

        img = PhotoImage(data=default_img_data)
        image.configure(image=img)
        image.image = img
    except UnboundLocalError:
        pokemon_name.config(text=f"Enter a valid ID (digit only unbonded)")
    except TclError:
        pokemon_name.config(text=f"Not a valid Image link")
        default_img = requests.get("https://www.iconsdb.com/icons/preview/white/square-xxlnotvalid.png")
        default_img_data = default_img.content

        img = PhotoImage(data=default_img_data)
        image.configure(image=img)
        image.image = img


default_img = requests.get("https://www.iconsdb.com/icons/preview/white/square-xxl.png")
default_img_data = default_img.content



window = Tk()
window.title("Pokemon")
window.geometry("300x200")

get_id = Entry(window)
get_id.pack()


pokemon_name = Label(window, text="Enter the pokemon ID above ")
pokemon_name.pack()

show_btn = Button(window, text="show info", command=lambda: main_func())
show_btn.pack()

img = PhotoImage(data=default_img_data)

image = Label(window, image=img)
image.pack()

window.mainloop()



