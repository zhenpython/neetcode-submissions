CREATE TABLE stocks (
  id INTEGER PRIMARY KEY generated always as identity,
  name TEXT,
  transaction_dates DATE[]
);

-- Do not modify above this line --

insert into stocks (name, transaction_dates) values
    ('AAPL', array['2007-02-09', '2007-02-10', '2007-02-11']::date[]),
    ('GOOG', array['2004-12-15', '2004-12-16']::date[]);





-- Do not modify below this line --
SELECT * FROM stocks;
