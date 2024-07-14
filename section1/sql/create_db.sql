CREATE TABLE cards_transfer (
    id SERIAL PRIMARY KEY,
    old_card INTEGER NOT NULL,
    new_card INTEGER NOT NULL,
    dt DATE NOT NULL
);

-- CREATE FUNC FOR CONTROL
CREATE OR REPLACE FUNCTION is_change(old_card_param INTEGER, new_card_param INTEGER)
RETURNS TEXT AS $$
DECLARE
    new_old_card INTEGER;
    record_table RECORD;
    for_while BOOLEAN;
    for_count INTEGER;
BEGIN
    -- check the record with the new and old card
    SELECT old_card, new_card INTO record_table FROM cards_transfer WHERE old_card = old_card_param AND new_card = new_card_param;
    IF record_table IS NULL THEN
        RETURN 'Карту можно поменять';
    END IF;

    -- values for variables for the loop
    for_while := TRUE;
    for_count := 1;

    -- loop for multiple requests
    WHILE for_while = TRUE LOOP
        SELECT old_card, new_card, dt INTO record_table FROM cards_transfer WHERE cards_transfer.new_card = record_table.old_card;

        -- check if there is an entry with such a card
        IF record_table IS NULL THEN
            for_while := FALSE;
        ELSE
            for_count := for_count + 1;
        END IF;

        -- control date and count
        IF for_count > 4 THEN
            IF AGE(CURRENT_DATE, record_table.dt) < interval '1 year' THEN
                RETURN 'Карту нельзя изменить. Измените ее ' || TO_CHAR(record_table.dt + interval '1 year', 'dd.mm.YYYY');
            ELSE
                RETURN 'Карту можно поменять';
            END IF;
        END IF;
    END LOOP;

    RETURN 'Карту можно поменять';
END;
$$ LANGUAGE plpgsql;
