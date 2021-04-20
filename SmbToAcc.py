import sublime
import sublime_plugin
import re


class SmbToAccCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()

		for sel in sels:

			str = self.view.substr(sel)

			# Sub out inline equations
			inline_eqns = re.findall(r'\$[^\$]*\$',str)
			str = re.sub(r'\$[^\$]*\$','$inline_eqn$',str)

			# Velka pismena s hacky
			VH_in = [r'\+T',r'\+R',r'\+S',r'\+D',r'\+C',r'\+N']
			VH_out = ['Č','Ř','Š','Ď','Č','Ň']
			# Velka pismena s carkami
			VC_in = [r'\=E',r'\=U',r'\=I',r'\=O',r'\=A']
			VC_out = ['É','Ú','Í','Ó','Á']
			# mala pismena s hacky (pres hacek)
			MH_in = [r'\+t',r'\+r',r'\+s',r'\+d',r'\+c',r'\+n']
			MH_out = ['č','ř','š','ď','č','ň']
			# mala pismena s carkami (pres carky)
			MC_in = [r'\=e',r'\=u',r'\=i',r'\=o',r'\=a']
			MC_out = ['é','ú','í','ó','á']
			# vrchní řada
			VR_in = ['2','3','4','5','6','7','8','9','0']
			VR_out = ['ě','š','č','ř','ž','ý','á','í','é']
			# ú, ů
			UU_in = [r'\[',';']
			UU_out = ['ú','ů']

			Symbols_in = VH_in + VC_in + MH_in + MC_in + VR_in + UU_in
			Symbols_out = VH_out + VC_out + MH_out + MC_out + VR_out + UU_out

			# substitute symbols
			for i in range(len(Symbols_in)):
				str = re.sub(Symbols_in[i],Symbols_out[i],str)

			# sub in inline equations
			for eqn in inline_eqns:
				eqn_w = re.sub(r'\\',r'\\\\',eqn) # without accidental unicode char.s
				str = re.sub(r'\$inline_eqn\$',eqn_w,str,1)

			self.view.replace(edit,sel,str)
