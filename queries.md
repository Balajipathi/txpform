

CREATE TABLE public.customer_data (
    id integer NOT NULL,
    "Name" character varying NOT NULL,
    "Location" character varying NOT NULL,
    breakfast  character varying ,
    lunch character varying ,
    dinner character varying ,
    special_breakfast character varying ,
    special_breakfast_quantity character varying ,
    normal_breakfast character varying ,
    normal_breakfast_quantity character varying ,
    special_lunch character varying ,
    special_lunch_quantity character varying ,
    normal_lunch character varying ,
    normal_lunch_quantity character varying ,
    special_dinner character varying ,
    special_dinner_quantity character varying ,
    normal_dinner character varying ,
    normal_dinner_quantity character varying ,
    delivery_contact_number character varying NOT NULL,
    customer_type character varying ,
    delivery_date character varying ,
    delivery_address character varying ,
    google_location character varying ,
    order_value character varying ,
    ordered_at timestamp with time zone DEFAULT now() NOT NULL

);
