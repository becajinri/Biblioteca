
# Devolucao de um emprestimo 
img_devolucao = Image.open('devolucao.png')
img_devolucao = img_devolucao.resize((18,18))
img_devolucao = ImageTK.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda,command= lambda:control('retorno'),image=img_devolucao,compound= LEFT, anchor=NW, text='Devolucao de um emprestimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_devolucao.grid(row=4, column=0,sticky=NSEW,padx=5,pady=6)

# Livros emprestados no momento
img__livros_emprestados = Image.open('livros2.png')
img__livros_emprestados = img_devolucao.resize((18,18))
img__livros_emprestados = ImageTK.PhotoImage(img_devolucao)
b_livros_emprestados = Button(frameEsquerda,command=Lambda:control('ver_livro_emprestados') ,image=img_usuario,compound= LEFT, anchor=NW, text='Livros emprestados no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_livros_emprestados.grid(row=4, column=0,sticky=NSEW,padx=5,pady=6)


janela.mainloop()
