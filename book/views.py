from django import forms
from django.shortcuts import render, redirect
from .forms import CadOfertaC, CadOfertaV, CadOfertaVeMer, CadOfertaCoMer
from .models import BookCompra, BookVenda, BookCompraMerc, BookVendaMerc
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.contrib.auth.models import User


@login_required
def cadastros_compra(request):
    book_compra = BookCompra.objects.all()
    book_venda = BookVenda.objects.all()
    book_compra_merc = BookCompraMerc.objects.all()
    book_venda_merc = BookVendaMerc.objects.all()
    form_c = CadOfertaC(request.POST)
    form_v = CadOfertaV(request.POST)
    form_c_mer = CadOfertaCoMer(request.POST)
    form_v_mer = CadOfertaVeMer(request.POST)

    if request.method == 'POST':
        if "submit_form_c" in request.POST: #busca nome do Modal Botton
            if form_c.is_valid():
                a = form_c.save()
                a.save()
                return redirect('book')
        elif "submit_form_v" in request.POST: #busca nome do Modal Botton
            if form_v.is_valid():
                a = form_v.save()
                a.save()
                return redirect('book')
        elif "submit_form_c_mer" in request.POST: #busca nome do Modal Botton
            if form_c_mer.is_valid():
                a = form_c_mer.save()
                a.save()
                return redirect('book') 
        elif "submit_form_v_mer" in request.POST: #busca nome do Modal Botton
            if form_v_mer.is_valid():
                a = form_v_mer.save()
                a.save()
                return redirect('book')  
    else:
        form_c = CadOfertaC()
        form_v = CadOfertaV()
        form_c_mer = CadOfertaCoMer()
        form_v_mer = CadOfertaVeMer()
    return render(request, 'book_view.html', 
        {"book_compra": book_compra,
        "book_venda": book_venda, 
        "book_compra_merc": book_compra_merc,
        "book_venda_merc": book_venda_merc, 
        "form_c": form_c,
        "form_v": form_v,
        "form_c_mer": form_c_mer, 
        "form_v_mer": form_v_mer })


def delete_view_c_m(request, id):
    context = {}

    obj = get_object_or_404(BookCompraMerc, pk=id)
 
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/book")        
    return render(request, "delete_view.html", context)


def delete_view_v_m(request, id): 
    context ={}

    obj = get_object_or_404(BookVendaMerc, pk = id)     
 
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/book")        
    return render(request, "delete_view.html", context)


def delete_view_v(request, id): 
    context = {}

    obj = get_object_or_404(BookVenda, pk = id)     
 
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/book")        
    return render(request, "delete_view.html", context)


def delete_view_c(request, id):
    context = {}

    obj = get_object_or_404(BookCompra, pk = id)     
    
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/book")        
    return render(request, "delete_view.html", context)

#////////////////////////////////////////#EDITAR

def edit_view_c(request, id):

    oferts = BookCompra.objects.get(pk=id)
    form = CadOfertaC(request.POST or None, instance=oferts)
    if form.is_valid():
        form.save()
        return redirect("/book") 
    return render(request, "edit_view.html", {"form":form, "oferts":oferts })


def edit_view_v(request, id):

    oferts = BookVenda.objects.get(pk=id)
    form = CadOfertaV(request.POST or None,instance=oferts)
    if form.is_valid():
        form.save()
        return redirect("/book") 
    return render(request, "edit_view.html", {"form":form, "oferts":oferts })


def edit_view_c_m(request,id):
    oferts = BookCompraMerc.objects.get(pk=id)
    form = CadOfertaCoMer(request.POST or None,instance=oferts)
    if form.is_valid():
        form.save()
        return redirect("/book") 
    return render(request, "edit_view.html", {"form":form, "oferts": oferts})


def edit_view_v_m(request,id):
    oferts = BookVendaMerc.objects.get(pk=id)
    form = CadOfertaVeMer(request.POST or None,instance=oferts)
    if form.is_valid():
        form.save()
        return redirect("/book") 
    return render(request, "edit_view.html", {"form":form, "oferts":oferts })




        

