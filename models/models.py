# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class school(models.Model):
#     _name = 'school.school'
#     _description = 'school.school'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100




class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'
    name = fields.Char()
    
    class_id = fields.Many2one('school.school')

class teacher(models.Model):
    _name = 'school.teacher'
    _description = 'school.teacher'

    name = fields.Char()


class school(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    name = fields.Char()
    student = fields.One2many('school.student','class_id')
    teacher = fields.Many2many('school.teacher.name')



    




