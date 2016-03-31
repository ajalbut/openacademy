# -*- coding: utf-8 -*-
# © <2016> <Luis Felipe Mileo>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import fields, models, api


class Session(models.Model):

    _name = "openacademy.session"
    _description = "Session"

    name = fields.Char(
        string=u"Name",
        required=True,
    )
    start_date = fields.Date(
        string=u"Data de inicio", default=fields.Date.today
    )
    duration = fields.Integer(
        string=u"Duração (dias)"
    )
    seats = fields.Integer(
        string=u"Seats"
    )
    active = fields.Boolean(default=True)
    taken_seats = fields.Float(
        compute="_compute_taken_seats"
    )
    teacher_category = fields.Selection(
        selection=[
            ('level1', 'Level 1'),
            ('level2', 'Level 2')
        ],
        string="Teacher Category"
    )
    instructor_id = fields.Many2one(
        'res.partner', ondelete='set null', domain=[
            '|',
            ('is_instructor', '=', True),
            ('teacher_category', 'in',
             [n for n, l in teacher_category.selection])
        ]
    )

    course_id = fields.Many2one('openacademy.course', ondelete='cascade')
    attendee_ids = fields.One2many('openacademy.attendee', 'id')

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for r in self:
            if r.seats and r.seats > 0 and r.attendee_ids:
                r.taken_seats = 100 * len(r.attendee_ids) / r.seats
            else:
                r.taken_seats = 0.0

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message':
                        "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }
