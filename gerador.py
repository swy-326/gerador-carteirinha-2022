#!/usr/bin/python

import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import urllib.request as req
import pandas as pd


def add_text(nome, id, turno, new_img):

	myFont = ImageFont.truetype('NotoSans-Regular.ttf', 40)
	myFont2 = ImageFont.truetype('NotoSans-Regular.ttf', 25)

	new_img.text((315, 740), "Validade: 12/2022", font=myFont2, fill=(0,0,0))

	if (len(nome) > 23):
		new_img.text((540, 443), "ID: " + str(int(id)), font=myFont ,fill=(255,255,255))
		new_img.text((540, 493), "Turno: " + turno, font=myFont, fill=(255,255,255))

		nomes = nome.split(' ')

		count = 0
		primeira_linha = []
		while count < 25:
			primeira_linha.append(nomes[0])
			count += len(nomes[0])
			nomes.pop(0)

		new_img.text((540, 543), "Nome: " + ' '.join(nome for nome in primeira_linha), font=myFont, fill=(255,255,255))
		new_img.text((540, 593), ' '.join(nome for nome in nomes), font=myFont, fill=(255,255,255))

	else:
		new_img.text((540, 468), "ID: " + str(int(id)), font=myFont ,fill=(255,255,255))
		new_img.text((540, 518), "Turno: " + turno, font=myFont, fill=(255,255,255))
		new_img.text((540, 568), "Nome: " + nome, font=myFont, fill=(255,255,255))



def add_photo(photo_url, img):

	filename = photo_url.rsplit('/', 1)[-1]
	req.urlretrieve(photo_url, filename)

	photo = Image.open(filename)

	photo_resized = photo.resize((452, 603))
	img.paste(photo_resized, (72, 136))




def main():

	excel_path = sys.argv[1]

	df = pd.read_excel(excel_path, engine='openpyxl')

	for index, row in df.iterrows():

		# load base image
		img = Image.open('base.png')

		# load student informations from xlsx
		nome = row['Aluno']
		id = int(row['ID'])
		turno = row['Turno']
		photo_url = str(row['Foto'])

		# add photo to base image
		if 'http' in photo_url:
			add_photo(photo_url, img)

		# draw to base image
		new_img = ImageDraw.Draw(img)
		add_text(nome, id, turno, new_img)
		
		# save carteirinha
		img.save(str(id) + '.png')
	

if __name__ == "__main__":
	main()