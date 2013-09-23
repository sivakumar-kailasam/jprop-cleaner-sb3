import sublime, sublime_plugin

def extract_lines(view,edit):
	regions = [s for s in view.sel() if not s.empty]
	if not regions:
		regions = [sublime.Region(0,view.size())]
	for region in regions:
 		text = view.substr(region)
 		lines = text.splitlines()
 		return lines

def get_line_value_pair(lines,duplicate_keys):
 	i = 0
 	duplicate_keys_occurance = {}
 	result_lines=[]
	
 	for x in duplicate_keys:
 		duplicate_keys_occurance.setdefault(x,0)

 	for line in reversed(lines):
 		y = line.encode('ascii','ignore')
 		y = y.decode("utf-8")
 		pos = y.find('=')
		
 		if(pos != -1):
 			z = y[0:pos]
 			z = z.strip()
 			try:
 				if (duplicate_keys.index(z) > -1):
 					if (duplicate_keys_occurance[z] == 0):
 						result_lines.append(line)
 						duplicate_keys_occurance[z] = 1
 			except Exception as e:
 				result_lines.append(line)
 				pass
 		else:
 			result_lines.append(line)
 	return result_lines


def find_duplicate_keys(lines):
 	specific_keys = []
 	duplicate_keys  = []
 	for x in lines:
 			y = x.encode('ascii','ignore')
 			y = y.decode("utf-8")
 			pos = y.find("=")
			
 			if (pos != -1):
 				z = y[0:pos]
 				z = z.strip()
				
 				try:
 					if(specific_keys.index(z) > -1):
 						try:
 							if(duplicate_keys.index(z) > -1):
 								pass
 						except Exception as e1:
 							duplicate_keys.append(z)
 				except Exception as e:
 					specific_keys.append(z)
 	print ('Duplicate keys are : ', duplicate_keys)
 	return duplicate_keys
		

class JpcleanerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		lines = extract_lines(self.view, edit)
		duplicate_keys  = find_duplicate_keys(lines)
		result_lines = get_line_value_pair(lines,duplicate_keys)
		status  = ""
		if( len(duplicate_keys) ==0 ):
 			status = "No duplicates!!!!"
		else:	
 			regionToErase = sublime.Region(0, self.view.size())
 			self.view.erase(edit,regionToErase)
 			status = "Done cleaning duplicates! Save file after reviewing the changes!!!"
 			for line in reversed(result_lines):
 				loc = self.view.sel()[0].a
 				self.view.insert(edit, loc, line  +"\n")
		sublime.status_message("status")