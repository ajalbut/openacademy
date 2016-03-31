# -*- coding: utf-8 -*-
# © <2016> <Luis Felipe Mileo>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import fields, models


class Session(models.Model):

    _name = "openacademy.session"
    _description = "Session"

    name = fields.Char(
        string=u"Name",
        required=True,
    )
    start_date = fields.Date(
        string=u"Data de inicio",
    )
    duration = fields.Integer(
        string=u"Duração (dias)"
    )
    seats = fields.Integer(
        string=u"Seats"
    )

    instructor_id = fields.Many2one(
        'res.partner', ondelete='set null', domain=[
            '|',
            ('is_instructor', '=', True),
            ('category_id.name', 'ilike', 'teacher')
        ]
    )
    course_id = fields.Many2one('openacademy.course', ondelete='cascade')
    attendee_ids = fields.One2many('openacademy.attendee', 'id')
