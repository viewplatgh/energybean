from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
import csv, codecs, cStringIO

from feedback2013.models import Subject, Student, Score, Feedback


class UnicodeWriter:
	"""
	A CSV writer which will write rows to CSV file "f",
	which is encoded in the given encoding.
	"""

	def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
		# Redirect output to a queue
		self.queue = cStringIO.StringIO()
		self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
		self.stream = f
		self.encoder = codecs.getincrementalencoder(encoding)()

	def writerow(self, row):
		self.writer.writerow([s.encode("utf-8") for s in row])
		# Fetch UTF-8 output from the queue ...
		data = self.queue.getvalue()
		data = data.decode("utf-8")
		# ... and reencode it into the target encoding
		data = self.encoder.encode(data)
		# write to the target stream
		self.stream.write(data)
		# empty queue
		self.queue.truncate(0)

	def writerows(self, rows):
		for row in rows:
			self.writerow(row)
	
	def write(self, data):
		self.stream.write(data)

def simple_export_fb2013(request):
	response = HttpResponse(mimetype='text/csv')
	response['Content-Disposition'] = 'attachment; filename=feedback2013.csv'
	csvwriter = UnicodeWriter(response)
	csvwriter.write(codecs.BOM_UTF8)
	csvwriter.writerow([u'中文姓名', 
								u'英文姓名', 
								u'就读高中', 
								u'Email', 
								u'来澳前(中国)所读学校', 
								u'来澳前(中国)所学最高年级', 
								u'来澳年份', 
								u'最终ATAR成绩', 
								u'录取大学(校区)与专业', 
								u'意见建议',
								u'反馈发布时间',
								u'Unit3/4科目', 
								u'原始分', 
								u'加减分后', 
								u'是否为2013年所学，或为2012提前已考？', 
								u'备注',])
	for item in Feedback.objects.all():
		csvwriter.writerow([unicode(item.student.chinese_name), 
									unicode(item.student.english_name),
									unicode(item.student.high_school),
									unicode(item.student.email),
									unicode(item.student.school_in_china),
									unicode(item.student.education_in_china),
									unicode(item.student.year_study_in_au),
									unicode(item.student.final_atar_score),
									unicode(item.student.uni_and_major),
									unicode(item.comment),
									unicode(item.created_date)])
		for item2 in Score.objects.filter(student=item.student):
			csvwriter.writerow([unicode(),
										unicode(),
										unicode(),
										unicode(),
										unicode(),
										unicode(),
										unicode(),
										unicode(),
										unicode(),
										unicode(),
										unicode(),
										unicode(item2.subject.name),
										unicode(item2.study_score),
										unicode(item2.scaled_score),
										unicode('Yes' if item2.for_2012_2011 else 'No'),
										unicode(item2.remark)])
	return response		