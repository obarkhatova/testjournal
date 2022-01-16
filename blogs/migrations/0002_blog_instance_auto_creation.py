from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        ('users', '0002_user'),
    ]

    operations = [
        migrations.RunSQL(
            ('''
                    CREATE OR REPLACE FUNCTION create_blog()
                    RETURNS trigger LANGUAGE plpgsql AS
                        $$BEGIN
                            INSERT INTO blogs_blog
                            (title, created, author_id)
                            VALUES('', now(), NEW.id);                            
                            RETURN NEW;
                        END;                                                
                    $$;
                '''),
            ('''
                    DROP FUNCTION IF EXISTS create_blog();
                ''')
        ),

        migrations.RunSQL(
            ('''
                    CREATE TRIGGER default_blog_trg
                    AFTER INSERT ON users_user
                    FOR EACH ROW
                    EXECUTE PROCEDURE create_blog();
                '''),
            ('''
                    DROP TRIGGER IF EXISTS default_blog_trg ON
                    users_user;
                ''')
        ),
    ]

