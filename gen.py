# -*- coding: utf-8 -*-
import os, json

W = []
def A(s=''): W.append(s)
def T(k,v): A(f' data-i18n="{k}">{v}')

def btn(lbl, action, cls='px-4 py-2 rounded-xl font-bold text-sm hover:opacity-90 transition'):
    return f'<button onclick="{action}" class="{cls}">{lbl}</button>'

# ========== DOCTYPE + HEAD ==========
A('<!DOCTYPE html><html lang="it" class="light"><head>')
A('<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">')
A('<title>Banca del Tempo - ACLI</title>')
A('<script src="https://cdn.tailwindcss.com"></script>')
A('<script>tailwind.config={darkMode:"class"}</script>')
A('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">')
A('<style>')
A('.tc{display:none}.tc.on{display:block}')
A('@keyframes pg{0%,100%{box-shadow:0 0 0 0 rgba(245,158,11,.7)}50%{box-shadow:0 0 0 12px rgba(245,158,11,0)}}.pg{animation:pg 2s infinite}')
A('.cd{width:40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:8px;font-size:13px;transition:all .15s;cursor:pointer}')
A('.cd:not(.dis):hover{transform:scale(1.1);box-shadow:0 0 0 3px rgba(59,130,246,.4)}')
A('.cd.sel{background:#2563eb!important;color:#fff!important}')
A('.cd.tod{box-shadow:inset 0 0 0 2px #f59e0b}')
A('.cd.dis{opacity:.3;cursor:default;pointer-events:none}')
A('.cd.occ{background:#fecaca!important;color:#991b1b!important;cursor:not-allowed;pointer-events:none}')
A('.z2{transform:scale(2);transform-origin:top left;cursor:zoom-out!important}')
A('.pp{width:120px;height:120px;border-radius:50%;object-fit:cover;border:4px solid #2563eb}')
A('</style></head>')

# ========== BODY ==========
A('<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-100 font-sans flex flex-col min-h-screen">')

# ---------- HEADER ----------
A('<header class="bg-blue-900 dark:bg-slate-950 text-white shadow-lg sticky top-0 z-50"><div class="max-w-7xl mx-auto px-3 py-2 flex flex-col sm:flex-row flex-wrap justify-between items-center gap-2">')
A('<div class="flex items-center gap-2 cursor-pointer shrink-0" onclick="go(\'landing\')">')
A('<img src="assets/logo.jpg" class="w-10 h-10 rounded-lg object-contain bg-white p-0.5">')
A('<img src="assets/logo_acli.jpg" class="h-10 w-auto rounded-lg object-contain bg-white p-0.5">')
A('<div class="ml-1"><h1 class="text-lg font-bold leading-tight">Banca del Tempo</h1><p class="text-[10px] text-blue-200">ACLI Ceglie del Campo, Bari</p></div></div>')
A('<nav class="flex gap-1 text-xs font-medium overflow-x-auto w-full sm:w-auto items-center pb-1 sm:pb-0">')
navs=[('landing','Chi Siamo'),('missione','Missione'),('docenti','Docenti'),('progetti','Progetti'),('prenota','Prenota Ore'),('dashboard','Dashboard'),('donazioni','Donazioni')]
for tid,lbl in navs:
    ec=' text-amber-300' if tid=='donazioni' else ''
    A(f'<button onclick="go(\'{tid}\')" class="px-2 py-1.5 rounded-lg hover:bg-blue-800 dark:hover:bg-slate-800 transition whitespace-nowrap{ec}">{lbl}</button>')
A('<button id="navR" onclick="go(\'registrazione\')" class="px-2 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 font-bold transition whitespace-nowrap">Registrati</button>')
A('<button id="navP" onclick="go(\'impostazioni\')" class="px-2 py-1.5 rounded-lg hover:bg-blue-800 dark:hover:bg-slate-800 transition whitespace-nowrap text-emerald-300 hidden">Profilo</button>')
A('<button onclick="go(\'master\')" class="px-2 py-1.5 rounded-lg bg-amber-500 text-blue-950 font-semibold hover:bg-amber-400 transition ml-1 whitespace-nowrap">Admin</button>')
A('<div class="flex items-center gap-2 ml-2 border-l border-white/20 pl-2 shrink-0">')
A('<button onclick="tdk()" class="text-lg hover:text-amber-400 transition"><i class="fa-solid fa-moon" id="tIco"></i></button>')
A('<select id="lS" onchange="sL()" class="bg-blue-800 dark:bg-slate-800 text-white border-none rounded px-1 py-1 text-[10px] outline-none cursor-pointer"><option value="it">IT</option><option value="en">EN</option><option value="de">DE</option></select>')
A('</div></nav></div></header>')

A('<main class="flex-grow max-w-7xl w-full mx-auto p-4 sm:p-6">')

# ===== LANDING =====
A('<section id="landing" class="tc on space-y-8">')
A('<div class="bg-gradient-to-r from-blue-900 to-indigo-800 dark:from-slate-800 dark:to-slate-900 text-white rounded-2xl p-6 sm:p-10 shadow-xl flex flex-col md:flex-row items-center justify-between gap-6">')
A('<div class="space-y-4 max-w-2xl">')
A('<span class="bg-amber-500 text-blue-950 text-xs font-bold px-3 py-1 rounded-full uppercase">Scambio Intergenerazionale</span>')
A('<h2 class="text-3xl sm:text-4xl font-extrabold leading-tight">Colleghiamo la memoria e il futuro a Bari</h2>')
A('<p class="text-blue-100">La Banca del Tempo permette ai pensionati di mettere a disposizione la propria esperienza per giovani, extracomunitari e tutta la comunità.</p>')
A('<div class="pt-2 flex flex-wrap gap-3">')
A('<button onclick="go(\'registrazione\')" class="bg-emerald-600 text-white px-5 py-2.5 rounded-xl font-bold hover:bg-emerald-500 transition shadow-lg">Registrati Ora</button>')
A('<button onclick="go(\'docenti\')" class="bg-amber-500 text-blue-950 px-5 py-2.5 rounded-xl font-bold hover:bg-amber-400 transition">Esplora Docenti</button>')
A('<button onclick="go(\'missione\')" class="bg-white/10 backdrop-blur-md text-white border border-white/20 px-5 py-2.5 rounded-xl font-semibold hover:bg-white/20 transition">Scopri la Missione</button>')
A('<button onclick="openBP()" class="pg bg-amber-500 text-blue-950 px-5 py-2.5 rounded-xl font-bold hover:bg-amber-400 transition flex items-center gap-2"><i class="fa-solid fa-sitemap"></i> Visualizza Blueprint</button>')
A('</div></div>')
A('<div class="bg-white/10 backdrop-blur-md p-6 rounded-2xl border border-white/10 text-center min-w-[200px]"><div class="text-4xl font-extrabold text-amber-400">1.480</div><div class="text-xs uppercase tracking-wider text-blue-200 mt-1">Ore Erogate</div></div>')
A('</div>')
# IMG1
A('<div class="w-full rounded-2xl overflow-hidden shadow-lg h-64 sm:h-96 relative border border-slate-200 dark:border-slate-700">')
A('<img src="assets/img1.jpg" class="w-full h-full object-cover">')
A('<div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 to-transparent flex items-end p-6 sm:p-8"><div><h3 class="text-white font-bold text-2xl sm:text-3xl">Uniamo le generazioni</h3><p class="text-slate-200 text-sm mt-2">Condivisione, dialogo e supporto reciproco.</p></div></div></div>')
# ACLI
A('<div class="flex flex-col sm:flex-row items-center gap-4 bg-white dark:bg-slate-800 rounded-2xl p-6 border border-slate-200 dark:border-slate-700 shadow-sm">')
A('<img src="assets/logo_acli.jpg" class="h-20 w-auto rounded-xl object-contain bg-white p-1 shadow">')
A('<div class="text-center sm:text-left"><h4 class="font-bold text-blue-900 dark:text-blue-400 text-lg">Associazioni Cristiane Lavoratori Italiani</h4><p class="text-sm text-slate-600 dark:text-slate-400 mt-1">Programma di inclusione sociale - Sede ACLI Ceglie del Campo, Bari.</p><p class="text-xs text-slate-400 mt-2 italic">Logo ACLI a cura di <strong>Luigi Giovannelli</strong></p></div></div>')
# VALORI
A('<div class="grid md:grid-cols-3 gap-6">')
for icon,clr,title,desc in [('fa-graduation-cap','blue','Materie Teoriche','Matematica, Storia e materie scolastiche.'),('fa-hammer','amber','Mestieri Pratici','Potatura, agricoltura, cucina, manutenzione.'),('fa-handshake','emerald','Inclusione Sociale','Aperta a tutti: pensionati, giovani, extracomunitari.')]:
    A(f'<div class="bg-white dark:bg-slate-800 p-6 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm space-y-2"><div class="text-{clr}-600 dark:text-{clr}-400 text-2xl"><i class="fa-solid {icon}"></i></div><h3 class="font-bold text-lg dark:text-white">{title}</h3><p class="text-sm text-slate-600 dark:text-slate-400">{desc}</p></div>')
A('</div>')
# AREE
A('<div class="pt-8 border-t border-slate-200 dark:border-slate-700 space-y-4"><h3 class="text-2xl font-bold text-center dark:text-white">Aree di Insegnamento</h3><div class="grid grid-cols-2 md:grid-cols-3 gap-4">')
for icon,clr,area in [('fa-seedling','emerald','Agricoltura'),('fa-wrench','slate','Officina'),('fa-scissors','lime','Potatura'),('fa-utensils','orange','Cucina'),('fa-mug-hot','amber','Bar'),('fa-book-open','blue','Doposcuola')]:
    A(f'<div class="bg-{clr}-50 dark:bg-{clr}-900/20 p-4 rounded-xl border border-{clr}-100 dark:border-{clr}-800/50 flex flex-col items-center text-center hover:shadow-md transition"><div class="w-12 h-12 bg-{clr}-500 text-white rounded-full flex items-center justify-center text-xl mb-2"><i class="fa-solid {icon}"></i></div><h4 class="font-bold">{area}</h4></div>')
A('</div></div></section>')

# ===== MISSIONE =====
A('<section id="missione" class="tc space-y-8">')
A('<div class="text-center max-w-3xl mx-auto space-y-3"><span class="bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-400 text-xs font-bold px-3 py-1 rounded-full uppercase">Inclusione Sociale</span><h2 class="text-3xl font-extrabold dark:text-white">Lo Scopo del Nostro Programma</h2></div>')
A('<div class="bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-slate-800 dark:to-slate-900 rounded-2xl p-8 border border-blue-100 dark:border-slate-700 space-y-5 text-slate-700 dark:text-slate-300 leading-relaxed">')
for p in [
    'La <strong>Banca del Tempo ACLI</strong> è un programma di <strong>inclusione sociale</strong> ideato per <strong>reinserire attivamente nella comunità</strong> i cittadini che hanno terminato il proprio percorso lavorativo e sono andati in pensione.',
    'Molti pensionati possiedono competenze preziose acquisite in decenni di lavoro. La Banca del Tempo trasforma questa esperienza in una <strong>risorsa viva</strong> per il territorio, creando un ponte tra generazioni.',
    'Il programma si rivolge ai <strong>giovani</strong> in cerca di orientamento, alle <strong>persone extracomunitarie</strong> di condizione economica non agiata che necessitano di competenze professionali, e a <strong>tutti i cittadini</strong> che desiderano imparare o insegnare.',
    'La Banca del Tempo è <strong>aperta a tutti</strong>: italiani e stranieri, giovani e anziani, studenti e lavoratori. Nessuna barriera di età, nazionalità o condizione economica. L\'unico requisito è la volontà di partecipare.'
]: A(f'<p>{p}</p>')
A('</div>')
A('<div class="grid sm:grid-cols-3 gap-4">')
for icon,clr,t,d in [('fa-user-clock','amber','Pensionati','Tornano attivi trasmettendo le proprie competenze'),('fa-graduation-cap','blue','Giovani','Imparano mestieri e ricevono supporto scolastico'),('fa-earth-americas','emerald','Extracomunitari','Acquisiscono competenze per l\'inserimento lavorativo')]:
    A(f'<div class="bg-white dark:bg-slate-800 p-5 rounded-xl shadow-sm text-center border border-slate-100 dark:border-slate-700"><div class="text-3xl text-{clr}-500 mb-2"><i class="fa-solid {icon}"></i></div><h4 class="font-bold dark:text-white">{t}</h4><p class="text-xs text-slate-500 mt-1">{d}</p></div>')
A('</div>')
A('<div class="bg-white dark:bg-slate-800 rounded-2xl p-8 border border-slate-200 dark:border-slate-700 shadow-sm"><h3 class="text-xl font-bold dark:text-white mb-4">Come Funziona</h3><div class="grid sm:grid-cols-2 gap-4">')
for i,(t,d) in enumerate([('Iscrizione Gratuita','Compila il form con i tuoi dati anagrafici.'),('Scegli un Docente','Sfoglia il catalogo e trova la competenza.'),('Prenota sul Calendario','Seleziona giorno e fascia oraria.'),('Impara e Cresci','Partecipa alla lezione e accumula ore.')],1):
    A(f'<div class="flex gap-3"><div class="w-8 h-8 bg-blue-100 dark:bg-blue-900/30 text-blue-600 rounded-full flex items-center justify-center font-bold text-sm shrink-0">{i}</div><div><h4 class="font-semibold">{t}</h4><p class="text-sm text-slate-500">{d}</p></div></div>')
A('</div></div></section>')

print('Sections 1-2 done:', len(W))

# ===== REGISTRAZIONE =====
A('<section id="registrazione" class="tc max-w-3xl mx-auto space-y-6">')
A('<div class="text-center"><h2 class="text-2xl font-bold dark:text-white">Registrazione alla Banca del Tempo</h2><p class="text-sm text-slate-500">Compila tutti i campi per iscriverti gratuitamente.</p></div>')
A('<div id="regOk" class="hidden bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 rounded-2xl p-6 text-center space-y-3"><i class="fa-solid fa-circle-check text-emerald-500 text-4xl"></i><h3 class="font-bold text-emerald-800 dark:text-emerald-400 text-lg">Sei già registrato!</h3><p class="text-sm text-slate-600 dark:text-slate-400" id="regOkN"></p><button onclick="go(\'impostazioni\')" class="bg-blue-900 text-white px-6 py-2.5 rounded-xl font-bold hover:bg-blue-800 transition mt-2">Vai al Profilo</button></div>')
A('<form id="regF" class="bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-8 border border-slate-200 dark:border-slate-700 shadow-sm space-y-5">')
# Photo
A('<div class="flex flex-col items-center gap-3"><img id="phP" class="pp hidden"><div id="phH" class="w-28 h-28 rounded-full bg-slate-200 dark:bg-slate-700 flex items-center justify-center text-3xl text-slate-400"><i class="fa-solid fa-camera"></i></div><label class="cursor-pointer bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400 text-sm font-bold px-4 py-2 rounded-xl hover:bg-blue-200 transition"><i class="fa-solid fa-upload mr-1"></i> Carica Foto<input type="file" id="phI" accept="image/*" class="hidden"></label></div>')
# Fields
flds = [('rNome','Nome *','text'),('rCog','Cognome *','text'),('rDN','Data di Nascita *','date'),('rLN','Luogo di Nascita *','text')]
A('<div class="grid sm:grid-cols-2 gap-4">')
for fid,lbl,tp in flds:
    A(f'<div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">{lbl}</label><input type="{tp}" id="{fid}" required class="w-full p-2.5 border dark:border-slate-600 dark:bg-slate-700 dark:text-white rounded-lg text-sm outline-none focus:ring-2 focus:ring-blue-500"></div>')
A('<div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Sesso *</label><select id="rSesso" required class="w-full p-2.5 border dark:border-slate-600 dark:bg-slate-700 dark:text-white rounded-lg text-sm outline-none focus:ring-2 focus:ring-blue-500"><option value="">--</option><option value="M">Maschile</option><option value="F">Femminile</option></select></div>')
A('<div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Codice Fiscale *</label><input type="text" id="rCF" required maxlength="16" class="w-full p-2.5 border dark:border-slate-600 dark:bg-slate-700 dark:text-white rounded-lg text-sm uppercase outline-none focus:ring-2 focus:ring-blue-500"></div>')
A('</div>')
# Indirizzo
A('<div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Indirizzo Completo *</label><div class="grid sm:grid-cols-4 gap-3">')
for fid,ph,w in [('rVia','Via/Piazza','sm:col-span-2'),('rCiv','N.',''),('rCap','CAP',''),('rCom','Comune','')]:
    extra = f' {w}' if w else ''
    A(f'<div{extra if w else ""} class=""><input type="text" id="{fid}" required placeholder="{ph}" class="w-full p-2.5 border dark:border-slate-600 dark:bg-slate-700 dark:text-white rounded-lg text-sm outline-none focus:ring-2 focus:ring-blue-500"></div>')
A('<div><select id="rProv" required class="w-full p-2.5 border dark:border-slate-600 dark:bg-slate-700 dark:text-white rounded-lg text-sm outline-none focus:ring-2 focus:ring-blue-500"><option value="">Prov.</option>')
for p in ['BA','FI','MI','RM','NA','TO','PA','BO','GE','VE','PD','CT','CA','BR','LE','TA','FG','BT']: A(f'<option value="{p}">{p}</option>')
A('</select></div></div></div>')
# Contatti
A('<div class="grid sm:grid-cols-2 gap-4"><div><label class="block text-xs font-bold text-slate-500 uppercase mb-1">Telefono *</label><input type="tel" id="rTel" required class="w-full p-2.5 border dark:border-slate-600 dark:bg-slate-700 dark:text-white rounded-lg text-sm outline-none focus:ring-2 focus:ring-blue-500"></div>')
