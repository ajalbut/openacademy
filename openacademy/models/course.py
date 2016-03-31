# -*- coding: utf-8 -*-
# © <2016> <Luis Felipe Mileo>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields


class Course(models.Model):

    _name = "openacademy.course"
    _description = "Course"

    name = fields.Char(
        string="Title",
        required=True
    )
    description = fields.Text(
        string="Description"
    )

    responsible_id = fields.Many2one('res.users', ondelete='cascade')
    session_ids = fields.One2many('openacademy.session', 'id')
