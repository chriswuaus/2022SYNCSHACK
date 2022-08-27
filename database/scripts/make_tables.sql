CREATE TABLE groups (
    id UUID PRIMARY KEY,
    group_name VARCHAR(200) NOT NULL
);

CREATE TABLE units (
    id UUID PRIMARY KEY,
    unit_name VARCHAR(200) NOT NULL,
    unit_code VARCHAR(8) NOT NULL,
    unit_level SMALLINT NOT NULL,
    credit_points SMALLINT NOT NULL,
    academic_unit VARCHAR(100) NOT NULL,
    unit_description VARCHAR(1000) NOT NULL,
    available_semesters VARCHAR(1000) NOT NULL
);

CREATE TABLE unit_prerequisites (
    id UUID PRIMARY KEY,
    unit_id UUID NOT NULL,
    prerequisite_list VARCHAR(1000) NOT NULL,
    CONSTRAINT FK_prerequisite_unit_id FOREIGN KEY (unit_id) REFERENCES units(id)
);

CREATE TABLE unit_prohibitions (
    id UUID PRIMARY KEY,
    unit_id UUID NOT NULL,
    prohibition_list VARCHAR(1000) NOT NULL,
    CONSTRAINT FK_prohibition_unit_id FOREIGN KEY (unit_id) REFERENCES units(id)
);

CREATE TABLE unit_corequisites (
    id UUID PRIMARY KEY,
    unit_id UUID NOT NULL,
    corequisite_list VARCHAR(1000) NOT NULL,
    CONSTRAINT FK_corequisite_unit_id FOREIGN KEY (unit_id) REFERENCES units(id)
);

CREATE TABLE unit_assumed_knowledge (
    id UUID PRIMARY KEY,
    unit_id UUID NOT NULL,
    assumed_knowledge_list VARCHAR(1000) NOT NULL,
    CONSTRAINT FK_assumed_knowledge_unit_id FOREIGN KEY (unit_id) REFERENCES units(id)
);

CREATE TABLE unit_groups (
    id UUID PRIMARY KEY,
    unit_id UUID NOT NULL,
    group_id UUID NOT NULL,
    CONSTRAINT FK_unit_group_unit_id FOREIGN KEY (unit_id) REFERENCES units(id),
    CONSTRAINT FK_unit_group_group_id FOREIGN KEY (group_id) REFERENCES groups(id)
);

CREATE TABLE unit_reviews (
    id UUID PRIMARY KEY,
    unit_id UUID NOT NULL,
    rating SMALLINT NOT NULL,
    comment VARCHAR(500),
    CONSTRAINT FK_unit_reviews_unit_id FOREIGN KEY (unit_id) REFERENCES units(id)
);