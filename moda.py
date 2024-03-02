contagem=[]
números=[]
números2=[]
while True:
	k=input("Digite algo: ")
	números.append(k)
	if k not in números2:
		números2.append(k)
	r=input("Quer continuar?[S/N] ")
	if r in "Nn":
		break
	while r not in "Ss":
		r = input("Quer continuar?[S/N] ")
modaN1=0
for n in números2:
	modaN2=números.count(n)
	contagem.append(modaN2)
	if modaN2>modaN1:
		moda=n
		modaN1=modaN2
contagem=sorted(contagem)
z=len(contagem)-1
if len(números2)>1:
	try:
		if contagem[z]==contagem[z-1]:
			print("Não existe moda.")
		else:
			print("A moda da lista é {}, aparecendo {} vez(es).".format(moda, modaN1))
	except:
		print("A moda da lista é {}, aparecendo {} vez(es).".format(moda, modaN1))
else:
	print("A moda da lista é {}, aparecendo {} vez(es).".format(moda, modaN1))