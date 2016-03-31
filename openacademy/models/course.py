# -*- coding: utf-8 -*-
# © <2016> <Luis Felipe Mileo>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields, api, exceptions


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

    @api.constrains("name", "description")
    def _check_name_not_in_description(self):
        for r in self:
            if r.name == r.description:
                raise exceptions.ValidationError(
                    "The description cannot be in the name!"
                )

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    _sql_constraints = [
        ('name_unique_check',
         'UNIQUE(name)',
         "Duplicated name! The course name must be unique."),
    ]
