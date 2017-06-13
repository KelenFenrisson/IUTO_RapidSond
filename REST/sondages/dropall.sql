SET FOREIGN_KEY_CHECKS = 0;
SET GROUP_CONCAT_MAX_LEN=32768;
SET @tables = NULL;
SET @views = NULL;

SELECT GROUP_CONCAT('`', TABLE_NAME, '`') INTO @tables
  FROM information_schema.tables
  WHERE table_schema = (SELECT DATABASE());
SELECT IFNULL(@tables,'dummy') INTO @tables;
SET @tables = CONCAT('DROP TABLE IF EXISTS ', @tables);

SELECT GROUP_CONCAT('`', TABLE_NAME, '`') INTO @views
  FROM information_schema.views
  WHERE table_schema = (SELECT DATABASE());
SELECT IFNULL(@views,'dummy') INTO @views;
SET @views = CONCAT('DROP VIEW IF EXISTS ', @views);

PREPARE Tstmt FROM @tables;
EXECUTE Tstmt;
DEALLOCATE PREPARE Tstmt;

PREPARE Vstmt FROM @views;
EXECUTE Vstmt;
DEALLOCATE PREPARE Vstmt;

SET FOREIGN_KEY_CHECKS = 1;
