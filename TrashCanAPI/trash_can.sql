#DROP DATABASE IF EXISTS `innova2025`;
CREATE DATABASE IF NOT EXISTS `innova2025`;
USE innova2025;

-- TrashCans Table
CREATE TABLE trash_cans (
    trash_can_id INT PRIMARY KEY AUTO_INCREMENT,
    gps_latitude DECIMAL(9, 6),
    gps_longitude DECIMAL(9, 6),
    is_full BOOLEAN DEFAULT FALSE,  -- You can use 'true' or 'false' to indicate whether it's full
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Images Table (with foreign key to TrashCans)
CREATE TABLE images (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    trash_can_id INT,
    image_url VARCHAR(255),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trash_can_id) REFERENCES trash_cans(trash_can_id)
);

insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (1, 42.3394070, -71.0868608);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (2, 42.3398829, -71.0866291);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (3, 42.3402417, -71.0867961);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (4, 42.3404120, -71.0867558);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (5, 42.3409837, -71.0854743);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (6, 42.3414761, -71.0862526);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (7, 42.3411906, -71.0866496);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (16, 42.3393828, -71.0871835);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (17, 42.3387716, -71.0876064);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (18, 42.3389709, -71.0881322);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (19, 42.3389790, -71.0885834);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (20, 42.3393828, -71.0871835);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (21, 42.3390281, -71.0888818);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (22, 42.3388829, -71.0891655);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (23, 42.3391352, -71.0902286);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (24, 42.3394001, -71.0903614);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (25, 42.3397487, -71.0894366);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (26, 42.3394284, -71.0882039);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (27, 42.3388333, -71.0881944);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (28, 42.3381389, -71.0885556);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (29, 42.3380000, -71.0887778);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (30, 42.3378056, -71.0892222);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (31, 42.3376111, -71.0892778);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (32, 42.3385556, -71.0906667);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (33, 42.3386111, -71.0909444);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (38, 42.3388056, -71.0868611);
insert into trash_cans (trash_can_id, gps_latitude, gps_longitude) values (39, 42.3388056, -71.0870000);


insert into images (image_id, trash_can_id, image_url) values (1, 1, 'Trash Cans Cleaned/1/');
insert into images (image_id, trash_can_id, image_url) values (2, 2, 'Trash Cans Cleaned/2/');
insert into images (image_id, trash_can_id, image_url) values (3, 3, 'Trash Cans Cleaned/3/');
insert into images (image_id, trash_can_id, image_url) values (4, 4, 'Trash Cans Cleaned/4/');
insert into images (image_id, trash_can_id, image_url) values (5, 5, 'Trash Cans Cleaned/5/');
insert into images (image_id, trash_can_id, image_url) values (6, 6, 'Trash Cans Cleaned/6/');
insert into images (image_id, trash_can_id, image_url) values (7, 7, 'Trash Cans Cleaned/7/');
insert into images (image_id, trash_can_id, image_url) values (16, 16, 'Trash Cans Cleaned/16/');
insert into images (image_id, trash_can_id, image_url) values (17, 17, 'Trash Cans Cleaned/17/');
insert into images (image_id, trash_can_id, image_url) values (18, 18, 'Trash Cans Cleaned/18/');
insert into images (image_id, trash_can_id, image_url) values (19, 19, 'Trash Cans Cleaned/19/');
insert into images (image_id, trash_can_id, image_url) values (20, 20, 'Trash Cans Cleaned/20/');
insert into images (image_id, trash_can_id, image_url) values (21, 21, 'Trash Cans Cleaned/21/');
insert into images (image_id, trash_can_id, image_url) values (22, 22, 'Trash Cans Cleaned/22/');
insert into images (image_id, trash_can_id, image_url) values (23, 23, 'Trash Cans Cleaned/23/');
insert into images (image_id, trash_can_id, image_url) values (24, 24, 'Trash Cans Cleaned/24/');
insert into images (image_id, trash_can_id, image_url) values (25, 25, 'Trash Cans Cleaned/25/');
insert into images (image_id, trash_can_id, image_url) values (26, 26, 'Trash Cans Cleaned/26/');
insert into images (image_id, trash_can_id, image_url) values (27, 27, 'Trash Cans Cleaned/27/');
insert into images (image_id, trash_can_id, image_url) values (28, 28, 'Trash Cans Cleaned/28/');
insert into images (image_id, trash_can_id, image_url) values (29, 29, 'Trash Cans Cleaned/29/');
insert into images (image_id, trash_can_id, image_url) values (30, 30, 'Trash Cans Cleaned/30/');
insert into images (image_id, trash_can_id, image_url) values (31, 31, 'Trash Cans Cleaned/31/');
insert into images (image_id, trash_can_id, image_url) values (32, 32, 'Trash Cans Cleaned/32/');
insert into images (image_id, trash_can_id, image_url) values (33, 33, 'Trash Cans Cleaned/33/');
insert into images (image_id, trash_can_id, image_url) values (38, 38, 'Trash Cans Cleaned/38/');
insert into images (image_id, trash_can_id, image_url) values (39, 39, 'Trash Cans Cleaned/39/');
