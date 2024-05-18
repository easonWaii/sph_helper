"""3.10.1

Revision ID: 9486140d5733
Revises: b15f1db3dd33
Create Date: 2024-05-15 21:33:29.856343

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9486140d5733'
down_revision = 'b15f1db3dd33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vadmin_auth_dept', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_dept', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_menu', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_menu', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_role', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_role', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_user', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_user', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_help_issue', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_help_issue', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_help_issue_category', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_help_issue_category', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_record_login', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_record_login', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_record_sms_send', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_record_sms_send', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_resource_images', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_resource_images', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_dict_details', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_dict_details', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_dict_type', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_dict_type', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_settings', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_settings', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_settings_tab', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_settings_tab', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_comment='更新时间',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vadmin_system_settings_tab', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_settings_tab', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_settings', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_settings', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_dict_type', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_dict_type', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_dict_details', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_system_dict_details', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_resource_images', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_resource_images', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_record_sms_send', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_record_sms_send', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_record_login', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_record_login', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_help_issue_category', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_help_issue_category', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_help_issue', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_help_issue', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_user', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_user', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_role', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_role', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_menu', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_menu', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_dept', 'update_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='更新时间',
               existing_nullable=False)
    op.alter_column('vadmin_auth_dept', 'create_datetime',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('CURRENT_TIMESTAMP'),
               existing_comment='创建时间',
               existing_nullable=False)
    # ### end Alembic commands ###
