from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def about(request):
    scores = [
	{
		"Name": "Freya Ferrell",
		"Maths": 68,
		"Bio": 74,
		"Chem": 37,
		"English": 76
	},
	{
		"Name": "Jescie Clay",
		"Maths": 75,
		"Bio": 72,
		"Chem": 44,
		"English": 61
	},
	{
		"Name": "Axel Dalton",
		"Maths": 46,
		"Bio": 60,
		"Chem": 83,
		"English": 70
	},
	{
		"Name": "Gretchen Black",
		"Maths": 70,
		"Bio": 62,
		"Chem": 40,
		"English": 71
	},
	{
		"Name": "Serina Acevedo",
		"Maths": 44,
		"Bio": 66,
		"Chem": 84,
		"English": 69
	},
	{
		"Name": "Colin Moody",
		"Maths": 21,
		"Bio": 65,
		"Chem": 61,
		"English": 51
	},
	{
		"Name": "Iona Landry",
		"Maths": 60,
		"Bio": 68,
		"Chem": 76,
		"English": 50
	},
	{
		"Name": "Isaac Bartlett",
		"Maths": 60,
		"Bio": 48,
		"Chem": 58,
		"English": 65
	},
	{
		"Name": "Kirk Sexton",
		"Maths": 37,
		"Bio": 47,
		"Chem": 67,
		"English": 58
	},
	{
		"Name": "Moses Sampson",
		"Maths": 65,
		"Bio": 49,
		"Chem": 57,
		"English": 65
	},
	{
		"Name": "Fallon Sargent",
		"Maths": 68,
		"Bio": 78,
		"Chem": 32,
		"English": 77
	},
	{
		"Name": "Jerome Henson",
		"Maths": 54,
		"Bio": 44,
		"Chem": 70,
		"English": 76
	},
	{
		"Name": "Wilma Vazquez",
		"Maths": 43,
		"Bio": 79,
		"Chem": 46,
		"English": 60
	},
	{
		"Name": "Ian Frye",
		"Maths": 75,
		"Bio": 72,
		"Chem": 34,
		"English": 45
	},
	{
		"Name": "Erich Nieves",
		"Maths": 80,
		"Bio": 54,
		"Chem": 38,
		"English": 50
	},
	{
		"Name": "Harding Gillespie",
		"Maths": 52,
		"Bio": 48,
		"Chem": 71,
		"English": 49
	},
	{
		"Name": "Kameko Stokes",
		"Maths": 21,
		"Bio": 55,
		"Chem": 36,
		"English": 63
	},
	{
		"Name": "Zenaida Burris",
		"Maths": 59,
		"Bio": 78,
		"Chem": 52,
		"English": 52
	},
	{
		"Name": "Karyn Gentry",
		"Maths": 21,
		"Bio": 69,
		"Chem": 37,
		"English": 52
	},
	{
		"Name": "Kasimir Bartlett",
		"Maths": 44,
		"Bio": 70,
		"Chem": 43,
		"English": 77
	},
	{
		"Name": "Harrison Hurley",
		"Maths": 70,
		"Bio": 50,
		"Chem": 40,
		"English": 71
	},
	{
		"Name": "Tamara Perez",
		"Maths": 37,
		"Bio": 60,
		"Chem": 63,
		"English": 69
	},
	{
		"Name": "Jack Sharpe",
		"Maths": 47,
		"Bio": 54,
		"Chem": 53,
		"English": 45
	},
	{
		"Name": "Dana Fox",
		"Maths": 51,
		"Bio": 80,
		"Chem": 67,
		"English": 68
	},
	{
		"Name": "Wade Andrews",
		"Maths": 86,
		"Bio": 48,
		"Chem": 35,
		"English": 58
	},
	{
		"Name": "David Burton",
		"Maths": 70,
		"Bio": 72,
		"Chem": 45,
		"English": 54
	},
	{
		"Name": "Hoyt Russell",
		"Maths": 70,
		"Bio": 70,
		"Chem": 38,
		"English": 47
	},
	{
		"Name": "Addison Cantrell",
		"Maths": 80,
		"Bio": 80,
		"Chem": 34,
		"English": 54
	},
	{
		"Name": "Pandora Russell",
		"Maths": 80,
		"Bio": 59,
		"Chem": 47,
		"English": 60
	},
	{
		"Name": "Ori Walton",
		"Maths": 34,
		"Bio": 49,
		"Chem": 47,
		"English": 57
	},
	{
		"Name": "Camilla Horne",
		"Maths": 28,
		"Bio": 58,
		"Chem": 49,
		"English": 53
	},
	{
		"Name": "Geraldine Downs",
		"Maths": 59,
		"Bio": 67,
		"Chem": 31,
		"English": 54
	},
	{
		"Name": "Allegra Sexton",
		"Maths": 32,
		"Bio": 55,
		"Chem": 65,
		"English": 57
	},
	{
		"Name": "Xanthus Silva",
		"Maths": 65,
		"Bio": 74,
		"Chem": 51,
		"English": 72
	},
	{
		"Name": "Joseph Jimenez",
		"Maths": 72,
		"Bio": 54,
		"Chem": 87,
		"English": 66
	},
	{
		"Name": "Marsden Harris",
		"Maths": 29,
		"Bio": 63,
		"Chem": 67,
		"English": 69
	},
	{
		"Name": "Jarrod Barker",
		"Maths": 24,
		"Bio": 51,
		"Chem": 54,
		"English": 73
	},
	{
		"Name": "Keelie Guthrie",
		"Maths": 88,
		"Bio": 49,
		"Chem": 75,
		"English": 66
	},
	{
		"Name": "Hashim Palmer",
		"Maths": 50,
		"Bio": 47,
		"Chem": 72,
		"English": 70
	},
	{
		"Name": "Alfonso Brock",
		"Maths": 43,
		"Bio": 58,
		"Chem": 36,
		"English": 66
	},
	{
		"Name": "Beatrice Sampson",
		"Maths": 71,
		"Bio": 59,
		"Chem": 45,
		"English": 68
	},
	{
		"Name": "Armand Tucker",
		"Maths": 76,
		"Bio": 54,
		"Chem": 56,
		"English": 60
	},
	{
		"Name": "Althea Atkins",
		"Maths": 45,
		"Bio": 50,
		"Chem": 43,
		"English": 75
	},
	{
		"Name": "April Marshall",
		"Maths": 50,
		"Bio": 70,
		"Chem": 30,
		"English": 58
	},
	{
		"Name": "Cooper Holmes",
		"Maths": 51,
		"Bio": 79,
		"Chem": 61,
		"English": 50
	},
	{
		"Name": "Linda Noble",
		"Maths": 41,
		"Bio": 73,
		"Chem": 49,
		"English": 55
	},
	{
		"Name": "Lenore Sanchez",
		"Maths": 44,
		"Bio": 56,
		"Chem": 69,
		"English": 59
	},
	{
		"Name": "Melyssa Lowery",
		"Maths": 42,
		"Bio": 58,
		"Chem": 76,
		"English": 64
	},
	{
		"Name": "Nina Juarez",
		"Maths": 40,
		"Bio": 46,
		"Chem": 53,
		"English": 68
	},
	{
		"Name": "Gary Flores",
		"Maths": 48,
		"Bio": 45,
		"Chem": 68,
		"English": 72
	}]
    data ={
        "scores":scores,
    }
    return render(request, 'about.html',data)


def contact(request):

    age = 85
    weight = 33.99
    subjects = ["Maths", "Science", "Engineering"]
    isdisable = False
    name = "Sharon Obiri"

    data = {
        "age": age,
        "weight": weight,
        "subject": subjects,
        "isdisable": isdisable,
        "name": name
    }

    return render(request, 'product.html', data)