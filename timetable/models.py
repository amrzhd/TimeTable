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

class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    iranian_time = models.CharField(max_length=50, choices=iranian_time_slots, 
                                    default='9:00 - 9:45', null=False, blank=False)
    day = models.CharField(max_length=15, default='Sunday',choices=DAYS_OF_WEEK, null=False, blank=False) 
    
    def __str__(self):
        return f"{self.iranian_time} - {self.day}"
    
    @property
    def name(self):
        return f"{self.iranian_time} - {self.day}"
    
class FreeSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    iranian_time = models.CharField(max_length=50, choices=iranian_time_slots, 
                                    default='9:00 - 9:45', null=False, blank=False)
    day = models.CharField(max_length=15, default='Sunday',choices=DAYS_OF_WEEK, null=False, blank=False)
    
    def __str__(self):
        return f"{self.iranian_time} - {self.day}"
    
    @property
    def name(self):
        return f"{self.iranian_time} - {self.day}"
    
    # @property
    # def chinese_time(self):
    #     pass
        
class SectionTeacher(models.Model):
    teacher = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher}/{self.section}"
    
    class Meta:
        unique_together = [
            'teacher',
            'section',
        ]
    
class FreeSectionTeacher(models.Model):
    teacher = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    free_section = models.ForeignKey(FreeSection, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher}/{self.free_section}"
    
    class Meta:
        unique_together = [
            'teacher',
            'free_section',
        ]