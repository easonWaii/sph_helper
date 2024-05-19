"""3.10.1

Revision ID: 5a2510c25366
Revises: 9486140d5733
Create Date: 2024-05-19 07:48:34.114333

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5a2510c25366'
down_revision = '9486140d5733'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('platform_baseinfo_cookie',
    sa.Column('uniq_id', sa.String(length=50), nullable=False, comment='平台标识id'),
    sa.Column('nick_name', sa.String(length=50), nullable=False, comment='昵称'),
    sa.Column('finder_name', sa.String(length=255), nullable=True, comment='finder_name'),
    sa.Column('session_id', sa.String(length=255), nullable=True, comment='session_id'),
    sa.Column('platform_name', sa.String(length=50), nullable=True, comment='平台名称'),
    sa.Column('head_img_url', sa.String(length=255), nullable=False, comment='头像url'),
    sa.Column('last_login_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='最近访问时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键ID'),
    sa.Column('create_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='创建时间'),
    sa.Column('update_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='更新时间'),
    sa.Column('delete_datetime', sa.DateTime(), nullable=True, comment='删除时间'),
    sa.Column('is_delete', sa.Boolean(), nullable=False, comment='是否软删除'),
    sa.PrimaryKeyConstraint('id'),
    comment='cookie表'
    )
    op.create_index(op.f('ix_platform_baseinfo_cookie_finder_name'), 'platform_baseinfo_cookie', ['finder_name'], unique=False)
    op.create_index(op.f('ix_platform_baseinfo_cookie_head_img_url'), 'platform_baseinfo_cookie', ['head_img_url'], unique=False)
    op.create_index(op.f('ix_platform_baseinfo_cookie_nick_name'), 'platform_baseinfo_cookie', ['nick_name'], unique=False)
    op.create_index(op.f('ix_platform_baseinfo_cookie_platform_name'), 'platform_baseinfo_cookie', ['platform_name'], unique=False)
    op.create_index(op.f('ix_platform_baseinfo_cookie_session_id'), 'platform_baseinfo_cookie', ['session_id'], unique=False)
    op.create_index(op.f('ix_platform_baseinfo_cookie_uniq_id'), 'platform_baseinfo_cookie', ['uniq_id'], unique=False)
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
    op.drop_index(op.f('ix_platform_baseinfo_cookie_uniq_id'), table_name='platform_baseinfo_cookie')
    op.drop_index(op.f('ix_platform_baseinfo_cookie_session_id'), table_name='platform_baseinfo_cookie')
    op.drop_index(op.f('ix_platform_baseinfo_cookie_platform_name'), table_name='platform_baseinfo_cookie')
    op.drop_index(op.f('ix_platform_baseinfo_cookie_nick_name'), table_name='platform_baseinfo_cookie')
    op.drop_index(op.f('ix_platform_baseinfo_cookie_head_img_url'), table_name='platform_baseinfo_cookie')
    op.drop_index(op.f('ix_platform_baseinfo_cookie_finder_name'), table_name='platform_baseinfo_cookie')
    op.drop_table('platform_baseinfo_cookie')
    # ### end Alembic commands ###
