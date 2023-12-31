from django.db import models
from accounts.models import User
from django.utils import timezone

chinese_time_slots = (
    ('4:30 - 5:15', '4:30 - 5:15'),
    ('5:30 - 6:15', '5:30 - 6:15'),
    ('6:30 - 7:15', '6:30 - 7:15'),
    ('7:30 - 8:15', '7:30 - 8:15'),
    ('8:30 - 9:15', '8:30 - 9:15'),
    ('9:30 - 10:15', '9:30 - 10:15'),
    ('10:30 - 11:15', '10:30 - 11:15'),
    ('11:30 - 12:15', '11:30 - 12:15'),
    ('12:30 - 13:15', '12:30 - 13:15'),
    ('13:30 - 14:15', '13:30 - 14:15'),
    ('14:30 - 15:15', '14:30 - 15:15'),
    ('15:30 - 16:15', '15:30 - 16:15'),
    ('16:30 - 17:15', '16:30 - 17:15'),
)

iranian_time_slots = (
    ('9:00 - 9:45', '9:00 - 9:45'),
    ('10:00 - 10:45', '10:00 - 10:45'),
    ('11:00 - 11:45', '11:00 - 11:45'),
    ('12:00 - 12:45', '12:00 - 12:45'),
    ('13:00 - 13:45', '13:00 - 13:45'),
    ('14:00 - 14:45', '14:00 - 14:45'),
    ('15:00 - 15:45', '15:00 - 15:45'),
    ('16:00 - 16:45', '16:00 - 16:45'),
    ('17:00 - 17:45', '17:00 - 17:45'),
    ('18:00 - 18:45', '18:00 - 18:45'),
    ('19:00 - 19:45', '19:00 - 19:45'),
    ('20:00 - 20:45', '20:00 - 20:45'),
    ('21:00 - 21:45', '21:00 - 21:45'),
)

DAYS_OF_WEEK = (
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

MONTHS_OF_YEAR = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
)

class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    iranian_time = models.CharField(max_length=50, choices=iranian_time_slots, 
                                    default='9:00 - 9:45', null=False, blank=False)
    chinese_time = models.CharField(max_length=50, choices=chinese_time_slots, 
                                    default='4:30 - 5:15', null=False, blank=False)
    day = models.CharField(max_length=15, default='Sunday',choices=DAYS_OF_WEEK, null=False, blank=False)
    month = models.CharField(max_length=15, default='January',choices=MONTHS_OF_YEAR, null=False, blank=False)
    year = models.CharField(max_length=15, default='2023',null=False, blank=False)
    
    def __str__(self):
        return f"{self.chinese_time}/ {self.iranian_time} - {self.day} - {self.month}"
    
    @property
    def name(self):
        return f"{self.chinese_time}/ {self.iranian_time} - {self.day} - {self.month}"
        
class Class(models.Model):
    student_name = models.CharField(null=False, blank=False, max_length=50)
    session = models.PositiveBigIntegerField()
    platform = models.CharField(null=True, blank=True, max_length=50)
    
    def __str__(self):
        return f"{self.student_name}: session({self.session}) - platform: {self.platform}"
    
class SectionTeacher(models.Model):
    teacher = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, blank=False, null=True, on_delete=models.CASCADE)
    section_class = models.ForeignKey(Class, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.teacher}: {self.section} - {self.section_class}"
    
class FreeSectionTeacher(models.Model):
    teacher = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    section_class = models.ForeignKey(Class, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.teacher}: {self.section} - {self.section_class}"
